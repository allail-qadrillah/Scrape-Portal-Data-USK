import requests
from bs4 import BeautifulSoup
import os
import re
import time
import xlrd
import json


class PortalUSK:
    def __init__(self):
      self.baseURL = "https://data.unsyiah.ac.id/public/pengajar_prodi"
    
    def timer(func):
      """
      Decorator untuk mendapatkan lama waktu eksekusi kode dengan format dua angka dibelakang koma  
      """
      def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        print(f"Time taken : {(endTime - startTime):.2f} seconds")
        return result
      return wrapper

    @timer
    def getPesertaKelas(self, semester, jenjang, pembatasan, kode, kelas, peserta = 1, delay = 1) -> 'list':
      """
      Mendapatkan daftar peserta kelas dan mengembalikan dalam Dictionary.
      Jika list tidak ditemukan kemungkinan dikarenakan server memberikan data kosong, maka program akan terus meminta hingga server memberikan data. 
      jika kelasnya memang kosong, maka return None. oleh karena itu parameter peserta harus diisi

      @param semester: Semester yang akan diambil. ex : 20223 
      @param jenjang: jenjang sarjana. ex : 1
      @param pembatasan: pembatasan tiap jurusan berbeda. ex : 0410501 
      04 = fakultas, 10 = strata, 05 = jurusan, 01 = status mahasiwa (reguler?) 
      @param kode: kode kelas. ex : TLE102
      @param kelas: nama kelas. ex : 11
      @param peserta: peserta yang ada didalam kelas, default = 1
      jika pesertanya tidak 0 maka lakukan scrapping
      @param delay: waktu tunggu request ke server jika tidak meresponse. default 1 seconds

      """
      requests.packages.urllib3.disable_warnings()
      try:
        listStudent = None
        print(f'Scrapping Student Course {kelas} kode {kode} | ', end="")
        if int(peserta) != 0:
          while not listStudent:
            response = requests.post(self.baseURL + '/detail', verify=False, 
                      data={"semester": semester,
                            "jenjang": jenjang,
                            "pembatasan": pembatasan,
                            "kode": kode,
                            "kelas": kelas,
                            })
            pattern = re.compile(r'<td style=\\".*?\">(.*?)<\\/td>', re.IGNORECASE)
            listStudent = pattern.findall(response.text)
            if not listStudent: 
              print("Portal USK tidak memberikan response, mencoba ulang ...")
              time.sleep(delay)

        return [
            {
                "no": listStudent[i],
                "kode": listStudent[i+1],
                "kelas": listStudent[i+2],
                "npm": listStudent[i+3],
                "nama": listStudent[i+4],
                "kelamin": listStudent[i+5]
            } for i in range(0, len(listStudent), 6)
        ]          
      except TypeError:
        print("Kelas tidak ada mahasiswa")
        return None

      except Exception as e:
        print(e)

    @timer
    def getMataKuliah(self, semester = "20223", jenjang="#", fakultas='#', prodi = '#'):
      """
      Mendapatkan daftar kelas dan mengembalikannya dalam Dictionary

      @param semester: Semester yang akan diambil. ex: 20223 
      @param jenjang: jenjang sarjana, ex: 1
      @params fakultas: code urutan fakultas, ex: 04
      @params prodi: code urutan prodi, ex: 0410501
      """
      print(f"Scrapping Portal USK fakultas: {fakultas} | prodi: {prodi} => ", end="")
      try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(self.baseURL + '/get_box4', verify=False,
                    data={
                        "semester": semester,
                        "jenjang": jenjang,
                        "fakultas": fakultas,
                        "prodi": prodi,
                      })
        soup = BeautifulSoup(json.loads(response.content)[1], 'html.parser')
        listCourse = [i.text for i in soup.find_all('td')]
        listCodeGetStudent = soup.find_all('a')

        return [
          {
              "no": listCourse[value],
              "kode": listCourse[value+1],
              "nama": listCourse[value+2],
              "kelas": listCourse[value+3],
              "koordinator": listCourse[value+4],
              "ruang": listCourse[value+5],
              "hari": listCourse[value+6],
              "waktu": listCourse[value+7],
              "peserta": listCourse[value+8],
              "keterangan": listCourse[value+9],
              "kode-peserta":
              {
                  "data-kode": listCodeGetStudent[index].get('data-kode'),
                  "data-kelas": listCodeGetStudent[index].get('data-kelas'),
                  "data-semester": listCodeGetStudent[index].get('data-semester'),
                  "data-jenjang": listCodeGetStudent[index].get('data-jenjang'),
                  "data-pembatasan": listCodeGetStudent[index].get('data-pembatasan'),
              }
          } for index, value in enumerate(range(0, len(listCourse), 10))
        ]
      except Exception as e:
        print(e)

    def writeJson(self, path, data, createIfNotExist=True):
      """
      menulis file kedalam format .json
      @params path: path untuk menulis file, ex: './path/file.json'
      @params data: data yang akan ditulis (dict)
      @params createIfNotExists: jika file tidak ada maka akan dibuat (default = True)
      """
      if createIfNotExist:
        try:
          if not os.path.exists(path):
            print(f'create path {path}')
            os.makedirs(os.path.dirname(path))
        except FileExistsError as f:
          pass

      with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=2)

    def loadJson(self, path):
      return json.loads( open(path).read() )

    def getExcel(self, path, sheet = 0):
      """
      Mendapatkan data dari excel dan mengembalikan dalam list
      @param path: lokasi file
      @param sheet : list sheet. default = 0
      """
      workbook = xlrd.open_workbook(path)
      worksheet= workbook.sheet_by_index(sheet)

      return [worksheet.row_values(i) for i in range(1, worksheet.nrows)]

    def findCourses(self, namePerson, data):
      """
      mengembalikan list matakuliah yang diambil seseorang
      @param namePerson (string) : nama seseorang
      @param data (list): data yang diambil
      """
      course = []
      for courses in data:
        if courses['peserta'] != None:
          for peserta in courses["peserta"]:
            if peserta["nama"] == namePerson:
              course.append({
                  "no": courses["no"],
                  "kode": courses["kode"],
                  "nama kelas": courses["nama kelas"],
                  "kelas": str(int(courses['kelas'])),
                  "koordinator": courses["koordinator"],
                  "ruang": courses["ruang"],
                  "hari": courses["hari"],
                  "waktu": courses["waktu"]
              })
      return course

    def findCoursesFromDir(self, path, namePerson):
      course = []
      for folder in os.listdir(path):
        for file in ( os.listdir(path + '/' + folder) ):
          data = self.loadJson( path + '/' + folder + '/' + file )
          course.append( self.findCourses(namePerson, data) )
      return course
import requests
import re
import time
import xlrd
import json


class PortalUSK:
    def __init__(self):
      self.baseURL = "https://data.unsyiah.ac.id/public/pengajar_prodi/detail"
    
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
    def getPesertaKelas(self, semester, jenjang, pembatasan, kode, kelas) -> 'dict':
      """
      Mendapatkan daftar peserta kelas dari portal USK dan mengembalikan dalam Dictionary.
      Jika list tidak ditemukan kemungkinan dikarenakan server memberikan data kosong, maka program akan terus meminta hingga server memberikan data. !tapi bagaimana jika kelasnya memang kosong?

      @param semester: Semester yang akan diambil. ex : 20223 
      @param jenjang: jenjang sarjana. ex : 1
      @param pembatasan: pembatasan tiap jurusan berbeda. ex : 0410501 
      04 = fakultas, 10 = strata, 05 = jurusan, 01 = status mahasiwa (reguler?) 
      @param kode: kode kelas. ex : TLE102
      @param kelas: nama kelas. ex : 11

      """
      requests.packages.urllib3.disable_warnings()
      listStudent = []
      try:
        while not listStudent:
          print(f'Get student class {kelas} kode {kode}')
          response = requests.post(self.baseURL, verify=False, 
                    data={"semester": semester,
                          "jenjang": jenjang,
                          "pembatasan": pembatasan,
                          "kode": kode,
                          "kelas": kelas,
                          })
          pattern = re.compile(r'<td style=\\".*?\">(.*?)<\\/td>', re.IGNORECASE)
          listStudent = pattern.findall(response.text)

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

      except Exception as e:
        print(e)
    
    def getExcel(self, path, sheet = 0):
      """
      Mendapatkan data dari excel dan mengembalikan dalam list
      @param path: lokasi file
      @param sheet : list sheet. default = 0
      """
      workbook = xlrd.open_workbook(path)
      worksheet= workbook.sheet_by_index(sheet)

      return [worksheet.row_values(i) for i in range(1, worksheet.nrows)]

    def writeData(self, pathSave, excelData):

      data = []
      for excel in excelData:
        dataStructure = {
            "no": int(excel[0]),
            "kode": excel[1],
            "nama kelas": excel[2],
            "kelas": excel[3],
            "koordinator": excel[4],
            "ruang": excel[5],
            "hari": excel[6],
            "waktu": excel[7],
            "keterangan": excel[8],
            "peserta": api.getPesertaKelas(
                semester="20223",
                jenjang="1",
                pembatasan="0410501",
                kode=excel[1],
                kelas=int(excel[3])
            )
        }
        data.append(dataStructure)

      with open(r'./Database/Teknik/Elektro.json', 'w') as outfile:
        json.dump(data, outfile)

    
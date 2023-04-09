import requests
from bs4 import BeautifulSoup
import re
import time
import json


class Scrape_Portal_USK:
    def __init__(self):
      self.pengajar_prodi_URL = "https://data.unsyiah.ac.id/public/pengajar_prodi"

    def getPesertaKelas(self, semester, jenjang, pembatasan, kode, kelas, peserta=1, delay=1, notResponse=10) -> 'list':
      """
      Mendapatkan daftar peserta kelas dan mengembalikan dalam Dictionary.
      Jika list tidak ditemukan kemungkinan dikarenakan server memberikan data kosong, maka program akan terus meminta hingga server memberikan data. 
      jika kelasnya memang kosong, maka return None. oleh karena itu parameter peserta harus diisi
      jika Portal USK terus menerus tidak memberikan response. maka skip aja kelasnya

      @param semester: Semester yang akan diambil. ex : 20223 
      @param jenjang: jenjang sarjana. ex : 1
      @param pembatasan: pembatasan tiap jurusan berbeda. ex : 0410501 
      04 = fakultas, 10 = strata, 05 = jurusan, 01 = status mahasiwa (reguler?) 
      @param kode: kode kelas. ex : TLE102
      @param kelas: nama kelas. ex : 11
      @param peserta: peserta yang ada didalam kelas, default = 1
      jika pesertanya tidak 0 maka lakukan scrapping
      @param delay: waktu tunggu request ke server jika tidak meresponse. default 1 seconds
      @param notResponse: jika Portal USK tidak response sebanyak notResponse maka skip kelasnya. default = 10
      """
      requests.packages.urllib3.disable_warnings()
      try:
        listStudent = None
        countNotResponse = 0
        print(f'Scrap {pembatasan} {kelas} kode {kode} | ', end="")
        if int(peserta) != 0:
          while not listStudent:
            response = requests.post(self.pengajar_prodi_URL + '/detail', verify=False,
                                     data={"semester": semester,
                                           "jenjang": jenjang,
                                           "pembatasan": pembatasan,
                                           "kode": kode,
                                           "kelas": kelas,
                                           })
            pattern = re.compile(
                r'<td style=\\".*?\">(.*?)<\\/td>', re.IGNORECASE)
            listStudent = pattern.findall(response.text)

            if not listStudent:
              print("Portal USK tidak memberikan response, mencoba ulang ...")
              countNotResponse += 1
              if countNotResponse == notResponse:
                print("--------------- Skip Kelas --------------- ")
                break
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


    def getMataKuliah(self, semester="20223", jenjang="#", fakultas='#', prodi='#'):
      """
      Mendapatkan daftar kelas dan mengembalikannya dalam Dictionary

      @param semester: Semester yang akan diambil. ex: 20223 
      @param jenjang: jenjang sarjana, ex: 1
      @params fakultas: code urutan fakultas, ex: 04
      @params prodi: code urutan prodi, ex: 0410501
      """
      print(
          f"Scrapping Portal USK fakultas: {fakultas} | prodi: {prodi} => ", end="")
      try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(self.pengajar_prodi_URL + '/get_box4', verify=False,
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





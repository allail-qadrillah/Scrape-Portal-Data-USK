import threading
from ScrapePortalUSK import PortalUSK
from timer import Timer
import json
import os
from config import URUTAN_FAKULTAS
api = PortalUSK()

@Timer
def getAllMataKuliah(path, urutanFakultas):

  for fakultas, code in urutanFakultas.items():
    mataKuliah = api.getMataKuliah(
      semester="20223",
      jenjang='1',
      fakultas= code
    )

    api.writeJson(f"{path}/{fakultas}.json", mataKuliah)

@Timer
def getAllPeserta(pathLoad, pathSave):
  for fakultas in os.listdir(pathLoad):
    courses = api.loadJson(f"{pathLoad}/{fakultas}")
    lenData = len(courses)
    pesertaMK = []
    for i, course in  enumerate(courses):
      print(f"persetase = { round( (i / lenData )*100, 2 ) }%")
      listPeserta = api.getPesertaKelas(
          semester=course['kode-peserta']['data-semester'],
          jenjang=course['kode-peserta']['data-jenjang'],
          pembatasan=course['kode-peserta']['data-pembatasan'],
          kode=course['kode-peserta']['data-kode'],
          kelas=course['kode-peserta']['data-kelas'],
          peserta= course['peserta']
      )
      pesertaMK.append({
          "no": course['no'],
          "kode": course['kode'],
          "nama kelas": course['nama'],
          "kelas": course['kelas'],
          "koordinator": course['koordinator'],
          "ruang": course['ruang'],
          "hari": course['hari'],
          "waktu": course['waktu'],
          "keterangan": course['keterangan'],
          "peserta": listPeserta
      })
    
      api.writeJson(
        f"{pathSave}/{fakultas[:-5]}/{course['keterangan']}.json", pesertaMK)

def getAllPesertaInThread(pathLoad, pathSave, fakultas, delay = 5):
  courses = api.loadJson(f"{pathLoad}/{fakultas}")
  pesertaMK = []
  for course in courses:
    listPeserta = api.getPesertaKelas(
        semester=course['kode-peserta']['data-semester'],
        jenjang=course['kode-peserta']['data-jenjang'],
        pembatasan=course['kode-peserta']['data-pembatasan'],
        kode=course['kode-peserta']['data-kode'],
        kelas=course['kode-peserta']['data-kelas'],
        peserta= course['peserta'],
        delay=delay
    )
    pesertaMK.append({
        "no": course['no'],
        "kode": course['kode'],
        "nama kelas": course['nama'],
        "kelas": course['kelas'],
        "koordinator": course['koordinator'],
        "ruang": course['ruang'],
        "hari": course['hari'],
        "waktu": course['waktu'],
        "keterangan": course['keterangan'],
        "peserta": listPeserta
    })
  
  api.writeJson(
      f"{pathSave}/{fakultas[:-5]}.json", pesertaMK)

@Timer
def getAllPesertaThread(pathLoad, pathSave):
  print("========== THREADING START ==========")
  fakultas = os.listdir(pathLoad)
  threads = []
  for fakultas in fakultas:
    t = threading.Thread(
      target= getAllPesertaInThread,
      args=(
          pathLoad, pathSave, fakultas, 
      )
    )
    threads.append(t)
    t.start()

  for t in threads:
    t.join()
  print(f"========== THREADING {t} COMPLETE ==========")


if __name__ == "__main__":
  # data = api.loadJson(
  #     './Database/teknik/TeknikS1Teknik Elektro.json')
  # print(api.findCoursesV2('NURYA MUFTIANA KHAIRANI', data))
  # print (
  #     api.findCoursesFromDir('./Database', 'M.AL-LAIL QADRILLAH'))
  # getAllMataKuliah('./Portal Data USK', URUTAN_FAKULTAS)
  # getAllPeserta('./Portal Data USK', './Database')
  getAllPesertaThread('./Portal Data USK', './Fakultas')
  # print(
  #     api.getPesertaKelas(
  #         semester= "20223",
  #         jenjang= "1",
  #         pembatasan= "0410101",
  #         kode= 'PTS106',
  #         kelas= "20",
  #         peserta = "1",
  #         delay=1
  #     )
  # )


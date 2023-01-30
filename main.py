import multiprocessing
from ScrapePesertaKelas import MiningPortalUSK
from ScrapePortalUSK import PortalUSK
from timer import Timer
import json
import os
from config import URUTAN_FAKULTAS, JURUSAN_TEKNIK, JURUSAN_KIP
import threading

@Timer
def MiningAllPesertaUSKS1():
  pathCourses = './COURSES USK S1'
  pathPeserta = './PESERTA COURSES USK S1'
  pathTeknikMK      = './Teknik MK'
  pathTeknikPeserta = './Teknik Peserta'
  pathKIPMK      = './KIP MK'
  pathKIPPeserta = './KIP Peserta'

  allPesertaKelas = MiningPortalUSK(
      pathLoad    = pathCourses,
      pathSave    = pathPeserta,
      urutanCode  = URUTAN_FAKULTAS
  )
  """
  untuk fakultas TEKNIK dan KIP dilakukan scapping secara terpisah
  karena datanya terlalu besar
  """
  teknik = MiningPortalUSK(
      pathLoad   = pathTeknikMK,
      pathSave   = pathTeknikPeserta,
      urutanCode = JURUSAN_TEKNIK,
  )
  
  kip = MiningPortalUSK(
      pathLoad   = pathKIPMK,
      pathSave   = pathKIPPeserta,
      urutanCode = JURUSAN_KIP,
  )

  allPesertaKelas.getAllMataKuliahFakultas()
  teknik.getAllMataKuliahProdi('04')
  kip.getAllMataKuliahProdi('06')

  mpAllPesertaKelas = multiprocessing.Process(
    target= allPesertaKelas.getAllPesertaThread
  )
  mpTeknik = multiprocessing.Process(
    target= teknik.getAllPesertaThread
  )
  mpKIP = multiprocessing.Process(
    target= kip.getAllPesertaThread
  )

  mpAllPesertaKelas.start()
  mpTeknik.start()
  mpKIP.start()

  # masukkan file json kedalam folder dengan nama yang sama
  allPesertaKelas.changeFileToFolder(pathPeserta, '.json')

  # pindakan folder TEKNIK dan KIP ke path seperti yang lainnya
  teknik.moveFolder(pathTeknikPeserta, pathCourses)
  kip.moveFolder(pathTeknikPeserta, pathCourses)
  
  mpAllPesertaKelas.join()
  mpTeknik.join()
  mpKIP.join()
  
@Timer
def MiningAllPesertaUSKS1V2():
  pathCourses = './COURSES USK S1'
  pathPeserta = './PESERTA COURSES USK S1'
  pathTeknikMK      = './Teknik MK'
  pathTeknikPeserta = './Teknik Peserta'
  pathKIPMK      = './KIP MK'
  pathKIPPeserta = './KIP Peserta'

  allPesertaKelas = MiningPortalUSK(
      pathLoad    = pathCourses,
      pathSave    = pathPeserta,
      urutanCode  = URUTAN_FAKULTAS
  )
  """
  untuk fakultas TEKNIK dan KIP dilakukan scapping secara terpisah
  karena datanya terlalu besar
  """
  teknik = MiningPortalUSK(
      pathLoad   = pathTeknikMK,
      pathSave   = pathTeknikPeserta,
      urutanCode = JURUSAN_TEKNIK,
  )
  
  kip = MiningPortalUSK(
      pathLoad   = pathKIPMK,
      pathSave   = pathKIPPeserta,
      urutanCode = JURUSAN_KIP,
  )

  # allPesertaKelas.getAllMataKuliahFakultas()
  # teknik.getAllMataKuliahProdi('04')
  # kip.getAllMataKuliahProdi('06')

  # allPesertaKelas.getAllPesertaThread()
  # teknik.getAllPesertaThread()
  # kip.getAllPesertaThread()

  # masukkan file json kedalam folder dengan nama yang sama
  # allPesertaKelas.changeFileToFolder(pathPeserta, '.json')

  # pindakan folder TEKNIK dan KIP ke path seperti yang lainnya
  # teknik.moveFolder(pathTeknikPeserta, pathCourses)
  kip.moveFolder(pathKIPPeserta, pathCourses)

import uvicorn
from fastapi import FastAPI

app = FastAPI()
  
@app.get('/')
def alwaysOnReplit():
  return "online"

@app.get('/scrape')
def scrapping():
  thread = threading.Thread(target=MiningAllPesertaUSKS1V2)
  thread.start()
  return "mining"

import logging
if __name__ == "__main__":

 # MiningAllPesertaUSKS1()
  logging.basicConfig(filename='log.txt', level=logging.DEBUG)
  logging.basicConfig(filename='log2.txt', level=logging.INFO)

  uvicorn.run(app, host="0.0.0.0", port=8000)
  # app = PortalUSK()
  # app.changeFileToFolder('./coba pindah', '.json')
  # app.changeFileToFolder(
  #   'coba pindah/file.json',
  #   './file/file.json',
  # )
  # mahasiswa = app.findCoursesFromDir(
  #   './DATABASE',
  #   'FATHURRAHMAN'
  # )

  # print(mahasiswa)

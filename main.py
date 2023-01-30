import logging
from fastapi import FastAPI
import uvicorn
import multiprocessing
from ScrapePesertaKelas import MiningPortalUSK
from ScrapePortalUSK import PortalUSK
from timer import Timer
import json
import os
from config import *
import threading


@Timer
def MiningAllPesertaUSKS1V2():
  pathCourses = './COURSES USK S1'
  pathPeserta = './PESERTA COURSES USK S1'

  # FT = MiningPortalUSK(
  #     pathLoad= pathCourses + '/FT',
  #     pathSave= pathPeserta + 'Teknik',
  #     urutanCode= JURUSAN_FT,
  # )
  # FT.getAllMataKuliahProdi(URUTAN_FAKULTAS['Teknik'])
  # FT.getAllPesertaThread()
  # FT.moveFolder(pathCourses + '/FT', pathPeserta + 'Teknik')

  FK = MiningPortalUSK(
      pathLoad=pathCourses + '/FK',
      pathSave=pathPeserta + 'Kedokteran',
      urutanCode=JURUSAN_FT,
  )
  FK.getAllMataKuliahProdi(URUTAN_FAKULTAS['Kedokteran'])
  FK.getAllPesertaThread()
  FK.moveFolder(pathCourses + '/FK', pathPeserta + 'Kedokteran')


app = FastAPI()


@app.get('/')
def alwaysOnReplit():
  return "online"


@app.get('/scrape')
def scrapping():
  thread = threading.Thread(target=MiningAllPesertaUSKS1V2)
  thread.start()
  return "mining"


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

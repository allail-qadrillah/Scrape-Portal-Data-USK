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
from mining import MiningAllPesertaUSKS1


app = FastAPI()
USK = PortalUSK()

@app.get('/getcourses')
async def getCourses( name: str,
                      fakultas: str = '',
                      jurusan: str=''):

    return USK.findCoursesFromDir(
        path        ='./PESERTA USK',
        namePerson  = name,
        nameFakultas= fakultas,
        nameProdi   = jurusan
    )

@app.get('/')
async def alwaysOnReplit():
  return "online"

@app.get('/scrape')
async def scrapping():
  thread = threading.Thread(target=MiningAllPesertaUSKS1)
  thread.start()
  return "mining"


if __name__ == "__main__":

  uvicorn.run(app,  port=8000)

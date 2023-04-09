from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# Konfigurasi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

  uvicorn.run(app,  host="0.0.0.0", port=8000)

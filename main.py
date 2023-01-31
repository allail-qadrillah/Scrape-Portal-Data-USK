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


@app.get('/')
def alwaysOnReplit():
  return "online"


@app.get('/scrape')
def scrapping():
  thread = threading.Thread(target=MiningAllPesertaUSKS1)
  thread.start()
  return "mining"


if __name__ == "__main__":

  uvicorn.run(app, host="0.0.0.0", port=8000)

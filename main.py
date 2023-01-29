import threading
from ScrapePesertaKelas import MiningPortalUSK
from ScrapePortalUSK import PortalUSK
from timer import Timer
import json
import os
from config import URUTAN_FAKULTAS


if __name__ == "__main__":
  app = PortalUSK()
  print(app.findCoursesFromDir(
    './DATABASE',
    'YOAN RIFQI CANDRA'
  ))



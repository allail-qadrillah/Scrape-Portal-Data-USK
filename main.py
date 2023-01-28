import threading
# from ScrapePesertaKelas import MiningMKFakultas
from ScrapePortalUSK import PortalUSK
from timer import Timer
import json
import os
from config import URUTAN_FAKULTAS

# api = MiningMKFakultas(
#     "./TEST LOAD",
#     "./TEST SAVE",
#     URUTAN_FAKULTAS
# )


if __name__ == "__main__":

  APP = PortalUSK()

  print(APP.findCoursesFromDir("./TEKNIK SAVE", 
  "IGO ICHSAN PRATAMA"))

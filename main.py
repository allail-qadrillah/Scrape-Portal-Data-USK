import threading
from ScrapePesertaKelas import MiningMKFakultas
from timer import Timer
import json
import os
from config import URUTAN_FAKULTAS

api = MiningMKFakultas(
    "./TEST LOAD",
    "./TEST SAVE",
    URUTAN_FAKULTAS
)


if __name__ == "__main__":

  api.getAllPesertaThread()

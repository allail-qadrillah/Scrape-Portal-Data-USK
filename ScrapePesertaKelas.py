import os
import threading
from config import URUTAN_FAKULTAS

from ScrapePortalUSK import PortalUSK

class MiningMKFakultas(PortalUSK):

  def __init__(self, pathLoad, pathSave, urutanFakultas):
    super().__init__()
    self.pathLoad = pathLoad
    self.pathSave = pathSave
    self.urutanFakultas = urutanFakultas


  def getAllMataKuliah(self):
    """
    mendapatkan semua matakuliah dari tiap fakultas  
    """
    for fakultas, code in self.urutanFakultas.items():
      mataKuliah =self.getMataKuliah(
          semester="20223",
          jenjang='1',
          fakultas=code
      )

      self.writeJson(f"{self.pathLoad}/{fakultas}.json", mataKuliah)

  def getAllPesertaKelas(self, pathFakultas, delay=5):
    """
    mendapatkan semua peserta kelas dari tiap fakultas
    @params pathFakultas: nama file json yang berisi daftar matakuliah dari tiap fakultas
    """
    courses = self.loadJson(f"{self.pathLoad}/{pathFakultas}")
    pesertaMK = []
    for course in courses:
      listPeserta = self.getPesertaKelas(
          semester=course['kode-peserta']['data-semester'],
          jenjang=course['kode-peserta']['data-jenjang'],
          pembatasan=course['kode-peserta']['data-pembatasan'],
          kode=course['kode-peserta']['data-kode'],
          kelas=course['kode-peserta']['data-kelas'],
          peserta=course['peserta'],
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

    self.writeJson(
        f"{self.pathSave}/{pathFakultas}", pesertaMK)

  def getAllPesertaThread(self):
  
    self.getAllMataKuliah()
    print("========== THREADING START ==========")
    threads = []
    for fakultas in os.listdir(self.pathLoad):
      print(fakultas)
      t = threading.Thread(
          target=self.getAllPesertaKelas,
          args=(fakultas, )
      )
      threads.append(t)
      t.start()

    for t in threads:
      t.join()
    print(f"========== THREADING {t} COMPLETE ==========")


URUTAN_FAKULTAS = {
    'kip': '06',
    'teknik': '04',
}
scrape = MiningMKFakultas(
  "./TEST LOAD",
  "./TEST SAVE",
  URUTAN_FAKULTAS
)

scrape.getAllPesertaThread()
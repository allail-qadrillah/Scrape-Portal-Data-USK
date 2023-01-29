import os
import threading
from config import URUTAN_FAKULTAS, JURUSAN_TEKNIK, JURUSAN_KIP

from ScrapePortalUSK import PortalUSK

class MiningPortalUSK(PortalUSK):

  def __init__(self, pathLoad, pathSave, urutanCode):
    super().__init__()
    self.pathLoad = pathLoad
    self.pathSave = pathSave
    self.urutanCode = urutanCode


  def getAllMataKuliahFakultas(self):
    """
    mendapatkan semua matakuliah dari tiap fakultas  
    """
    for fakultas, code in self.urutanCode.items():
      mataKuliah =self.getMataKuliah(
          semester="20223",
          jenjang='1',
          fakultas=code
      )

      self.writeJson(f"{self.pathLoad}/{fakultas}.json", mataKuliah)
  
  def getAllMataKuliahProdi(self, codeFakultas):
    """
    mendapatkan semua matakuliah dari tiap fakultas  
    """
    for fakultas, code in self.urutanCode.items():
      mataKuliah =self.getMataKuliah(
          semester="20223",
          jenjang='1',
          fakultas= codeFakultas,
          prodi=code
      )

      self.writeJson(f"{self.pathLoad}/{fakultas}.json", mataKuliah)

  def getAllPesertaKelas(self, pathFakultas, delay=5):
      """
      mendapatkan semua peserta kelas dari tiap fakultas
      @params pathFakultas: nama file json yang berisi daftar matakuliah dari tiap fakultas
      """
      courses = self.loadJson(f"{self.pathLoad}/{pathFakultas}")
      for course in courses:
          peserta = {
              "no": course['no'],
              "kode": course['kode'],
              "nama kelas": course['nama'],
              "kelas": course['kelas'],
              "koordinator": course['koordinator'],
              "ruang": course['ruang'],
              "hari": course['hari'],
              "waktu": course['waktu'],
              "keterangan": course['keterangan'],
              "peserta": self.getPesertaKelas(
                  semester=course['kode-peserta']['data-semester'],
                  jenjang=course['kode-peserta']['data-jenjang'],
                  pembatasan=course['kode-peserta']['data-pembatasan'],
                  kode=course['kode-peserta']['data-kode'],
                  kelas=course['kode-peserta']['data-kelas'],
                  peserta=course['peserta'],
                  delay=delay
              )}

          # cek apakah file sudah ada atau belum
          if os.path.exists(f"{self.pathSave}/{pathFakultas}"):
              # jika sudah, tambahkan data ke dalam file
              data = self.loadJson(f"{self.pathSave}/{pathFakultas}")
              data.append(peserta)
              self.writeJson(f"{self.pathSave}/{pathFakultas}", data)
          else:
              # jika belum, buat file baru dan tulis data pertama
              self.writeJson(f"{self.pathSave}/{pathFakultas}", [peserta])
  
  def mergeFromDirToJson(self, namaFile, pathSave):
    """
    menggabungkan semua file json yang ada didalam directory kedalam satu file json  
    """
    for pathJson in os.listdir(self.pathSave):

      for peserta in self.loadJson(self.pathSave + '/' + pathJson):
        if os.path.exists(pathSave + '/' + namaFile):
          load = self.loadJson(pathSave + '/' + namaFile)
          load.append(peserta)
          self.writeJson(pathSave + '/' + namaFile, load)
        else:
          self.writeJson(pathSave + '/' + namaFile, [peserta])

  def getAllPesertaThread(self):

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

def MiningAllPesertaUSK():
  pathCourses = './COURSES USK S1'
  pathPeserta = './PESERTA COURSES USK S1'

  allPesertaKelas = MiningPortalUSK(
                      pathCourses,
                      pathPeserta,
                      URUTAN_FAKULTAS
                    )
  allPesertaKelas.getAllPesertaThread()
  """
  untuk fakultas TEKNIK dan KIP dilakukan scapping secara terpisah
  karena datanya terlalu besar
  """
  teknik = MiningPortalUSK(
      "./TEKNIK LOAD",
      "./TEKNIK SAVE",
      URUTAN_FAKULTAS
  )

  teknik.mergeFromDirToJson('teknik.json', './DATABASE')

  # copy datanya kedalam pathPeserta


# URUTAN_FAKULTAS = {
#     'kip': '06',
#     # 'teknik': '04'
# }
# scrape = MiningPortalUSK(
#   "./KIP LOAD",
#   "./KIP SAVE",
#   JURUSAN_KIP
# )

# scrape.getAllMataKuliahProdi(codeFakultas='06')
# scrape.getAllPesertaThread()
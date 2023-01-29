import multiprocessing
from ScrapePesertaKelas import MiningPortalUSK
from ScrapePortalUSK import PortalUSK
from timer import Timer
import json
import os
from config import URUTAN_FAKULTAS, JURUSAN_TEKNIK, JURUSAN_KIP

@Timer
def MiningAllPesertaUSKS1():
  pathCourses = './COURSES USK S1'
  pathPeserta = './PESERTA COURSES USK S1'
  pathTeknikMK      = './Teknik MK'
  pathTeknikPeserta = './Teknik Peserta'
  pathKIPMK      = './KIP MK'
  pathKIPPeserta = './KIP Peserta'
  getMataKuliah  = True

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

if __name__ == "__main__":

  MiningAllPesertaUSKS1()

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

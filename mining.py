from timer import Timer
from ScrapePesertaKelas import MiningPortalUSK
from config import *

@Timer
def MiningAllPesertaUSKS1():
  pathCourses = './COURSES USK '
  pathPeserta = './PESERTA USK '
  # TEKNIK
  # FT = MiningPortalUSK(
  #     pathLoad= pathCourses + '/FT',
  #     pathSave= 'Teknik',
  #     urutanCode= JURUSAN_FT,
  # )
  # FT.getAllMataKuliahProdi(URUTAN_FAKULTAS['Teknik'])
  # FT.getAllPesertaThread()
  # FT.write_txt_file('log.txt', "===================== FT COMPLETE "=====================")
  # FT.moveFolder('Teknik', pathPeserta + '/Teknik')
  # # KIP
  # KIP = MiningPortalUSK(
  #     pathLoad=pathCourses + '/KIP',
  #     pathSave='KIP',
  #     urutanCode= JURUSAN_KIP,
  # )
  # KIP.getAllMataKuliahProdi(URUTAN_FAKULTAS['KIP'])
  # KIP.getAllPesertaThread()
  # KIP.write_txt_file('log.txt', ""===================== KIP COMPLETE "=====================")
  # KIP.moveFolder('KIP', pathPeserta + '/KIP')
  # # KEDOKTERAN
  # FK = MiningPortalUSK(
  #     pathLoad=pathCourses + '/FK',
  #     pathSave='Kedokteran',
  #     urutanCode= JURUSAN_FK,
  # )
  # FK.getAllMataKuliahProdi(URUTAN_FAKULTAS['Kedokteran'])
  # FK.getAllPesertaThread()
  # FK.write_txt_file('log.txt', ""===================== FK COMPLETE "=====================")
  # FK.moveFolder('Kedokteran', pathPeserta + '/Kedokteran')
  # EKONOMI
  FEB = MiningPortalUSK(
      pathLoad=pathCourses + '/FEB',
      pathSave='Ekonomi dan Bisnis',
      urutanCode= JURUSAN_FEB,
  )
  FEB.getAllMataKuliahProdi(URUTAN_FAKULTAS['Ekonomi'])
  FEB.getAllPesertaThread()
  FEB.write_txt_file('log.txt', ""===================== FEB COMPLETE "=====================")
  FEB.moveFolder('Ekonomi dan Bisnis', pathPeserta)
  # KEDOKTERAN HEWAN
  FKH = MiningPortalUSK(
      pathLoad=pathCourses + '/FKH',
      pathSave='Kedokteran Hewan',
      urutanCode= JURUSAN_FKH,
  )
  FKH.getAllMataKuliahProdi(URUTAN_FAKULTAS['Kedokteran Hewan'])
  FKH.getAllPesertaThread()
  FKH.write_txt_file('log.txt', ""===================== FKH COMPLETE "=====================")
  FKH.moveFolder('Kedokteran Hewan', pathPeserta)
  # KEDOKTERAN HUKUM
  FH = MiningPortalUSK(
      pathLoad=pathCourses + '/FH',
      pathSave='Hukum',
      urutanCode= JURUSAN_FH,
  )
  FH.getAllMataKuliahProdi(URUTAN_FAKULTAS['Hukum'])
  FH.getAllPesertaThread()
  FH.write_txt_file('log.txt', ""===================== FH COMPLETE "=====================")
  FH.moveFolder('Hukum', pathPeserta)
  # PERTANIAN
  FP = MiningPortalUSK(
      pathLoad=pathCourses + '/FP',
      pathSave='Pertanian',
      urutanCode= JURUSAN_FP,
  )
  FP.getAllMataKuliahProdi(URUTAN_FAKULTAS['Pertanian'])
  FP.getAllPesertaThread()
  FP.write_txt_file('log.txt', ""===================== FP COMPLETE "=====================")
  FP.moveFolder('Pertanian', pathPeserta)
  # MIPA
  MIPA = MiningPortalUSK(
      pathLoad=pathCourses + '/MIPA',
      pathSave='MIPA',
      urutanCode= JURUSAN_MIPA,
  )
  MIPA.getAllMataKuliahProdi(URUTAN_FAKULTAS['Mipa'])
  MIPA.getAllPesertaThread()
  MIPA.write_txt_file('log.txt', ""===================== MIPA COMPLETE "=====================")
  MIPA.moveFolder('MIPA', pathPeserta)
  # ISIP
  ISIP = MiningPortalUSK(
      pathLoad=pathCourses + '/ISIP',
      pathSave='ISIP',
      urutanCode= JURUSAN_FISIP,
  )
  ISIP.getAllMataKuliahProdi(URUTAN_FAKULTAS['Isip'])
  ISIP.getAllPesertaThread()
  ISIP.write_txt_file('log.txt', ""===================== ISIP COMPLETE "=====================")
  ISIP.moveFolder('ISIP', pathPeserta)
  # KELAUTAN DAN PERIKANAN
  KP = MiningPortalUSK(
      pathLoad=pathCourses + '/KP',
      pathSave='Kelautan dan Perikanan',
      urutanCode= JURUSAN_KP,
  )
  KP.getAllMataKuliahProdi(URUTAN_FAKULTAS['Kelautan dan Perikanan'])
  KP.getAllPesertaThread()
  KP.write_txt_file('log.txt', ""===================== KP COMPLETE "=====================")
  KP.moveFolder('Kelautan dan Perikanan', pathPeserta)
  # Keperawatan
  FKP = MiningPortalUSK(
      pathLoad=pathCourses + '/FKP',
      pathSave='Keperawatan',
      urutanCode= JURUSAN_FKP,
  )
  FKP.getAllMataKuliahProdi(URUTAN_FAKULTAS['Keperawatan'])
  FKP.getAllPesertaThread()
  FKP.write_txt_file('log.txt', ""===================== FKP COMPLETE "=====================")
  FKP.moveFolder('Keperawatan', pathPeserta)
  # Kedokteran Gigi
  FKG = MiningPortalUSK(
      pathLoad=pathCourses + '/FKG',
      pathSave='Kedokteran Gigi',
      urutanCode= JURUSAN_FISIP,
  )
  FKG.getAllMataKuliahProdi(URUTAN_FAKULTAS['Kedokteran Gigi'])
  FKG.getAllPesertaThread()
  FKG.write_txt_file('log.txt', ""===================== FKG COMPLETE "=====================")
  FKG.moveFolder('Kedokteran Gigi', pathPeserta)
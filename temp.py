from ScrapePortalUSK import PortalUSK
from timer import Timer
import json
api = PortalUSK()

def getMK(path, nama):
  data = api.loadJson(path)
  mk = api.findCourses(nama.upper(), data)
  return mk


@Timer
def main():
  data = {
      "semester": "20223",
      "jenjang": '1',
      "fakultas": '07',
      # "prodi": '0410501'
      "prodi": '#'
  }

  teknik = api.getMataKuliah(
      data['semester'],
      data['jenjang'],
      data['fakultas'],
      data['prodi']
  )
  # teknik = {
  #   'nama' : '1'
  # }
  api.writeJson('./Portal Data USK/Kedokteran.json', teknik)


@Timer
def getAllPeserta():
  courses = api.loadJson('./Portal Data USK/Kedokteran.json')
  pesertaMK = []
  lenData = len(courses)
  for i, course in enumerate(courses):
    print(f"persetase = { round( (i / lenData )*100, 2 ) }%")

    peserta = api.getPesertaKelas(
        semester=course['kode-peserta']['data-semester'],
        jenjang=course['kode-peserta']['data-jenjang'],
        pembatasan=course['kode-peserta']['data-pembatasan'],
        kode=course['kode-peserta']['data-kode'],
        kelas=course['kode-peserta']['data-kelas']
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
        "peserta": peserta
    })

    api.writeJson(
        f"./Database/Kedokteran/{course['keterangan']}.json", pesertaMK)

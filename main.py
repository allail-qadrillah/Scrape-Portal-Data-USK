from ScrapePortalUSK import PortalUSK
from timer import Timer
import json
api = PortalUSK()


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


if __name__ == "__main__":
  main()
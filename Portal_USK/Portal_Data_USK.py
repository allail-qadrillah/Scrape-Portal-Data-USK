from fuzzywuzzy import process
from .scrapping import Scrape_Portal_USK
from .util import util
import os


class PortalUSK(Scrape_Portal_USK,
                  util):

    def findCourses(self, namePerson, data):
      """
      mengembalikan list matakuliah yang diambil seseorang
      @param namePerson (string) : nama seseorang
      @param data (list): data yang diambil
      """
      course = []
      for courses in data:
        if courses['peserta'] != None:
          for peserta in courses["peserta"]:
            if peserta["nama"] == namePerson.upper():
              course.append({
                  "no": courses["no"],
                  "kode": courses["kode"],
                  "nama kelas": courses["nama kelas"],
                  "kelas": str((courses['kelas'])),
                  "koordinator": courses["koordinator"],
                  "ruang": courses["ruang"],
                  "hari": courses["hari"],
                  "waktu": courses["waktu"],
                  "peserta": {
                      "no": peserta["no"],
                      "kode": peserta["kode"],
                      "kelas": peserta["kelas"],
                      "npm": peserta["npm"],
                      "nama": peserta["nama"],
                      "kelamin": peserta["kelamin"],
                  }
              })
      return course

    def findCoursesFromDirJson(self, path, namePerson):
      """
      mencari matakuliah mahasiwa didalam folder yang terdapat file json

      @param path (string) : lokasi folder yang akan dicari
      @param namePerson (string) : nama mahasiswa yang akan dicari
      """
      course = []
      for folder in os.listdir(path):
          data = self.loadJson(path + '/' + folder)
          course.append(self.findCourses(namePerson, data))
      return course

    def findCoursesFromDir(self, path, namePerson,
                           nameFakultas='',
                           nameProdi=''):
      """
      mencari matakuliah mahasiswa yang diambil dari folder tertentu dan mengembalikannya dalam list

      @param path (string) : lokasi folder yang akan dicari
      @param namePerson (string) : nama mahasiswa yang akan dicari
      @param iterateFolder (boolean) : apakah folder akan di looping?
      """
      course = []

      for files in os.listdir(path):
        # jika mencari dengan nama fakultas
        if nameFakultas != '' and nameProdi == '':
          if nameFakultas == self.getFileName(files):
            data = self.findCoursesFromDirJson(
                path + '/' + nameFakultas, namePerson)
            course.append([i for i in data if i != []])
        # jika mencari dengan nama fakultas dan prodi
        elif nameFakultas != '' and nameProdi != '':
          if nameFakultas == self.getFileName(files):
            for file in os.listdir(path + '/' + files):
              if nameProdi == self.getFileName(file):
                data = self.loadJson(path + '/' + files + '/' + file)
                course.append(self.findCourses(namePerson, data))
        # jika hanya mencari dengan nama aja
        else:
          for file in os.listdir(path + '/' + files):
            data = self.loadJson(path + '/' + files + '/' + file)
            course.append(self.findCourses(namePerson, data))

      return [i for i in course if i != []]

    def get_all_nama_mahasiswa(self, path_load, path_save):
      """
      mengembalikan semua nama mahasiswa yang ada di dalam folder tertentu
      """
      mahasiswa = []
      for folders in os.listdir(path_load):
        for files in os.listdir(path_load + '/' + folders):
          kelas = self.loadJson(path_load + '/' + folders + '/' + files)
          for matakuliah in kelas:
            try:
              
              for peserta in matakuliah['peserta']:
                if peserta != None:
                  mahasiswa.append({
                      'nama': peserta['nama'],
                      'npm': peserta['npm'],
                      'kelamin': peserta['kelamin'],
                  })

            except TypeError:
              continue

      return self.writeJson(path_save, self.filter_duplicate_dict(mahasiswa))

    def find_similar_name(self, path, search, limit=5):
      names = self.load_nama_from_json(path)
      data_mahasiswa = self.loadJson(path)
    
      match = process.extract(search, names, limit=limit)
      nama_mirip = [
          {'bobot': nama[1], 'nama': mahasiswa['nama'],
              'npm': mahasiswa['npm'], 'kelamin': mahasiswa['kelamin']}
          for mahasiswa in data_mahasiswa
          for nama in match
          if mahasiswa['nama'] == nama[0]
      ]
      return sorted(nama_mirip, key=lambda value: value['bobot'], reverse=True)
        


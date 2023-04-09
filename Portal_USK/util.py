import os
import os
import xlrd
import json
import shutil


class util:
    def getFileName(self, file):
      """
      mengenbalikan nama file tanpa format filenya
      """
      return os.path.splitext(file)[0]

    def writeJson(self, path, data, createIfNotExist=True):
      """
      menulis file kedalam format .json
      @params path: path untuk menulis file, ex: './path/file.json'
      @params data: data yang akan ditulis (dict)
      @params createIfNotExists: jika file tidak ada maka akan dibuat (default = True)
      """
      if createIfNotExist:
        try:
          if not os.path.exists(path):
            print(f'create path {path}')
            os.makedirs(os.path.dirname(path))
        except FileExistsError as f:
          pass

      with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=2)

    def loadJson(self, path):
      return json.loads(open(path).read())

    def getExcel(self, path, sheet=0):
      """
      Mendapatkan data dari excel dan mengembalikan dalam list
      @param path: lokasi file
      @param sheet : list sheet. default = 0
      """
      workbook = xlrd.open_workbook(path)
      worksheet = workbook.sheet_by_index(sheet)

      return [worksheet.row_values(i) for i in range(1, worksheet.nrows)]

    def moveFolder(self, source, destination):
      return shutil.move(source, destination)

    def createFolder(self, path):
      return os.makedirs(path, exist_ok=True)

    def changeFileToFolder(self, path, formatFile):
      """
      memindahkan file menjadi kedalam folder
      @params path: lokasi file
      @params formatFile: format file yang akan diubah ke folder 
      """
      for file in os.listdir(path):
        if file.endswith(formatFile):
          pathMove = os.path.splitext(path + '/' + file)[0] + '/' + file
          self.createFolder(pathMove)
          self.moveFolder(path + '/' + file, pathMove)
    
    def filter_duplicate_dict(self, list_dict):
      return [dict(tupleized) for tupleized in set(
          tuple(item.items()) for item in list_dict)]

    def load_nama_from_json(self, path):
      return [item['nama'] for item in self.loadJson(path)]

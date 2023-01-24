import xlrd
import re
from bs4 import BeautifulSoup

response ="""[true,"\n <div class=\"col-md-12 box-detail\">\n <div class=\"table-responsive\">\n <table id=\"table3\" class=\"table
      table-striped table-bordered\" style=\"width:100%;\">\n <thead>\n <tr style=\"background:#2b3643;color:#fff;\">\n
          <th style=\\"font-size:11pt;padding:8px;\">No<\ /th>\n
          <th style=\\"font-size:11pt;padding:8px;\">Kode<\ /th>\n
          <th style=\\"font-size:11pt;padding:8px;\">Kelas<\ /th>\n
          <th style=\\"font-size:11pt;padding:8px;\">NPM<\ /th>\n
          <th style=\\"font-size:11pt;padding:8px;\">Nama<\ /th>\n
          <th style=\\"font-size:11pt;padding:8px;\">Kelamin<\ /th>\n <\ /tr>\n <\ /thead>\n
      <tbody>\n <tr>\n <td style=\\"width:20px;font-size:11pt;padding:8px;\">1<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">FEB102<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">68<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">2201101010012<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">LUDFIA NISRINA<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">P<\ /td>\n <\ /tr>\n
        <tr>\n <td style=\\"width:20px;font-size:11pt;padding:8px;\">2<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">FEB102<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">68<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">2201101010110<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">FITRA RIZKI ANANDA<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">L<\ /td>\n <\ /tr>\n
        <tr>\n <td style=\\"width:20px;font-size:11pt;padding:8px;\">3<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">FEB102<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">68<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">2201101010127<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">AGUS HILDANI<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">P<\ /td>\n <\ /tr>\n
        <tr>\n <td style=\\"width:20px;font-size:11pt;padding:8px;\">4<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">FEB102<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">68<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">2201101010141<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">SITI TSABITA<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">P<\ /td>\n <\ /tr>\n
        <tr>\n <td style=\\"width:20px;font-size:11pt;padding:8px;\">5<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">FEB102<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">68<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">2201101010143<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">MUHAMMAD RIZKI ISMAYA PUTRA<\ /td>\n
          <td style=\\"font-size:11pt;padding:8px;\">L<\\ /td>\n <\ /tr>\n <\ /tbody>\n <\ /table>\n <\ /div>\n <\ /div>\n
                        <br>\n "]"""

path = r'./Portal Data/Portal Data Teknik Elektro.xlsx'

# Membuka file xlsx
workbook = xlrd.open_workbook(path)

# Memilih sheet pertama
worksheet = workbook.sheet_by_index(0)

# Menampilkan perbaris tanpa judul
for i in range(1, worksheet.nrows):
    print(worksheet.row_values(i))
    break

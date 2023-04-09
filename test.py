from Portal_USK import PortalUSK

PATH_DATABASE = './DATABASE'

USK = PortalUSK()

# satu_nama = USK.findCoursesFromDir(
#     path=PATH_DATABASE+'/PESERTA USK',
#     namePerson='Galuh Putri Sabikha'
# )
# multiple_nama = USK.findCoursesFromDir(
#     path=PATH_DATABASE+'/PESERTA USK',
#     namePerson = 'Fathurrahman'
# )

# print(
#     USK.get_all_nama_mahasiswa(
#         path_load=PATH_DATABASE+'/PESERTA USK',
#         path_save=PATH_DATABASE+'/nama_mahasiswa2.json'
#     )
# )


# from fuzzywuzzy import process
# data_mahasiswa = USK.loadJson(PATH_DATABASE+'/nama_mahasiswa.json')
# names = USK.load_nama_from_json(PATH_DATABASE+'/nama_mahasiswa.json')
# name_to_search = "Wahyuda"
# match = process.extract(name_to_search, names, limit=5)

# nama_mirip = [
#     {'bobot' : nama[1], 'nama' : mahasiswa['nama'], 'npm' : mahasiswa['npm'], 'kelamin' : mahasiswa['kelamin']}
#     for mahasiswa in data_mahasiswa
#     for nama in match
#     if mahasiswa['nama'] == nama[0]
# ]
# nama_mirip = sorted(nama_mirip, key=lambda value: value['bobot'], reverse=True)

# # Menampilkan hasil yang diurutkan
# print(nama_mirip)
print(
    USK.find_similar_name(
        PATH_DATABASE+'/nama_mahasiswa.json', 'abikha')
)

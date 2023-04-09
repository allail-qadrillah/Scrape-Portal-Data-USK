from fuzzywuzzy import process

# Nama-nama yang tersedia
names = ["John Doe", "Jane Smith",
        "Michael Johnson", "David Brown", "Emily Taylor"]
# Nama yang dicari
name_to_search = "Johsn"
# Mencari nama yang mirip dengan yang dicari
match = process.extract(name_to_search, names, limit=3)
# Cetak nama yang ditemukan dan skor kemiripannya
print(match)

data = [
    {
        'no': '1',
        'pekerjaan': 'dokter',
        'identitas': [
            {
                'nama': 'allail',
                'umur': 30
            },
            {
                'nama': 'qadri',
                'umur': 20
            },
            {
                'nama': 'lil',
                'umur': 15
            },
        ]},
    {
        'no': '2',
        'pekerjaan': 'polisi',
        'identitas': [
            {
              'nama': 'randi',
              'umur': 30
            },
            {
                'nama': 'allail',
                'umur': 20
            },
            {
                'nama': 'lel',
                'umur': 15
            },
        ]
    }
]


def findPekerjaan(namaOrang, data):
    listPekerjaan = []
    for pekerjaan in data:
      for v in range( len(pekerjaan['identitas']) ):
        if pekerjaan['identitas'][v]['nama'] == namaOrang:
          listPekerjaan.append({
              "no": pekerjaan['no'],
              "pekerjaan": pekerjaan['pekerjaan'],
          })

    return listPekerjaan


def main():
    repeat = True
    while repeat:
        for i in range(10):
            if i == 5:
                repeat = True
                continue
            repeat = False
            print(i)


web = {
    '1': 'https:example.com/1',
    '2': 'https:example.com/2',
    '3': 'https:example.com/3',
}



# Membuat thread untuk setiap website
# threads = []
# for key in web:
#     print(key)
def find_number(n):
    i = 1
    digits = len(str(i))
    while digits < n:
        i += 1
        digits += len(str(i))
    return int(str(i)[n-digits-1])



print(find_number(1111))

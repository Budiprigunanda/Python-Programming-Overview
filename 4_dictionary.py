# dictionary = 'key', 'value'
employee= {
    'nama': 'Andy',
    'usia': 20,
    'married': True,
    'jabatan': 'IT Engineer',
    'kendaraan': ['mobil', 'motor'],
    'address': {
        'street': 'Jalan Mawar',
        'RT': 5,
        'RW': 2,
        'zipcode': 12345,
        'geo': {
            'lat': 12345.621271,
            'long': 1232131.12313
        }
    }
}

print(employee)
print("Value di dalam key 'nama' adalah:", employee['nama'])
print(list(employee.keys()))
print("Value di dalam key 'kendaraan' adalah:", employee['kendaraan'])
print("Value di dalam key 'kendaraan' di index pertama:", employee['kendaraan'][0])
#                                                         ['mobil', 'motor][0] = 'mobil'
print("Value di dalam key 'address' adalah:", employee['address'])
print("Value di dalam key 'address' nama jalan saja:", employee['address']['street'])
#                                                       ['mobil', 'motor][0] = 'mobil'

print(list(employee.keys()))
print(list(employee.values()))


# GET
print(employee.get('nama'))
print(employee.get('gaji', 'Key Not Found'))

# Assign Value baru ke Key yang juga baru
employee['gaji'] = 2000000
print(employee)

# Update Value di key yang sudah ada
employee['gaji'] = 3000000
print(employee)

# .update untuk mengupdate key dan value
employee.update({'NIK': 92131231, 'BPJS': 10000002121})
print(employee)

# .item = cara untuk ngambil list
print(list(employee.items()))
print(list(employee['address'].items()))
print(list(employee['address']['geo'].items()))

# cari value apakah ada di dictionary atau tidak
print('cari value 3000000 ada atau ngga?: ', 3000000 in employee.values())

# cari value terkecil atau tertinggi di dalam dictionary
nilai_ujian = {
    'Fisika': 82,
    'Matematika': 65,
    'Sejarah': 75
}

print('Mata pelajaran yang nilainya paling rendah: ', min(nilai_ujian, key=nilai_ujian.get))
print('Mata pelajaran yang nilainya paling tinggi: ', max(nilai_ujian, key=nilai_ujian.get))

# mengganti nama key
employee['alamat'] = employee.pop('address')
print(employee)

# menggabungkan 2 dictionary
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Fourty': 40, 'Fifty': 50, 'Sixty': 60}

# .update
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

# cara ke-2
dict1_dict2 = {*dict1, *dict2}
print(dict1_dict2)

# membuat dictionary dari 2 buah list
key = ['Ten', 'Twenty', 'Thirty']
value = [10, 20, 30]

sample_dict = dict(zip(key, value))
sample_dict_reserved = dict(zip(value, key))

print(sample_dict)
print(sample_dict_reserved)

sampe_list = list(zip(key, value))
print('ini sample list', sampe_list)

sample_tuple = tuple(zip(key,value))
print('in sampe tuple', sample_tuple)

sample_dict_test = {*key, *value}
print(sample_dict_test)

karyawan - ['Doni', 'Fiki', 'Akbar']


'''
No. 1
Masukkan hari: Senin 
output: bahasa inggris dari Senin adalah Monday

No. 2
Masukkan hari (INA/ENG): senin
output: bahasa inggris dari senin adalah Monday

Masukkan hari (INA/ENG): monday
output: bahasa indonesia dari monday adalah Senin
'''




# hari_dict = {
#     'senin': 'monday',
#     'selasa': 'tuesday',
#     'rabu': 'wednesday',
#     'kamis': 'thursday',
#     'jumat': 'friday',
#     'sabtu': 'saturday',
#     'minggu': 'sunday'
# }

# hari = input('masukan hari: ')
# print(f"bahasa inggris dari {hari.upper()} adalah {hari_dict[hari].uppper()}")




# Terjemahan2= {
#     '(INA/ENG)': {
#         'Senin': 'Monday'
#     }
# }
# print("bahasa inggris dari senin adalah:", Terjemahan2['(INA/ENG)']['Senin'])


# hari_list = list(hari_dict.keys())
# day_list = list(hari_dict.value())

# user_input = input("Masukkan hari (INA/ENG): ")

# if user_input in hari_list:
#     day = day_list[hari_list.index(user_input)]
#     print(f"Bahasa Inggris")
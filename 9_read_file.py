# data = open('kata.txt', 'r') # r = read
# # print(data.read())
# # text = data.read()
# # print(text)

# lines = data.readlines()
# # print(lines)
# # for line in lines :
# #     print(line)


# # data2 = open('kata2.txt', 'w') #w => write
# # data2.write('Ini dibuat di Python')

# data3 = open('kata3.txt', 'w') #w => write
# data3.write("print('Ini dibuat di Python')")

# abc = open('nama.txt', 'r')
# # text = (abc.read()).replace(',', '')
# #     'Andi, Budi, Caca'.replace(',', '')
# # print(text)
# text_list = (abc.read()).split(', ')
# print(text_list)

# list_nama = open('list_nama.text', 'w')
# for i in text_list:
#     list_nama.write(f'{i}\n')

data_diri = open('daftar_nama.csv', 'r')
x = data_diri.read().split('\n')
print(x)

header_list = x[0]
print('header list:', header_list)
header_element = header_list.split(',')
print('header element', header_element)

value_list = x[1:]
print(value_list)

data = []
for i in value_list: # ['Andi,21,Jakarta', 'Budi,22,Bandung', 'Caca,23,Jakarta']
    a = i.split(',')
    header_value = dict(zip(header_element, a))
    data.append(header_value)

# print(data)

json = open('daftar_nama.json', 'r')
print(json.read())

import json
with open('daftar_nama.json', mode='r') as daftar:
    output = json.load(daftar)

print(output[0])
print(type(output))
for i in range(len(output)):
    print(output[i])

output.append({'nama': 'Dede', 'usia': 24, 'kota': 'Bekasi'})

print(output)
with open('daftar_nama_update.json', 'w') as update:
    json.dump(output, update)


import csv

list_data = []
with open('daftar_nama.csv', 'r') as nama:
    read = csv.DictReader(nama)
    for data in read:
        list_data.append(dict(data))

print(list_data)
list_data.append({'nama': 'Dede', 'usia': 24, 'kota': 'Bekasi'})


with open('daftar_nama_update.csv', 'w') as update:
    columns = list_data[0].keys()
    write = csv.DictWriter(update, fieldnames=columns)
    write.writeheader()
    write.writerows(list_data)


print(columns)




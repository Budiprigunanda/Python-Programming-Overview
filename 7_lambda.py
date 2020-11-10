# ## LAMBDA ##

# def perkalian(a,b):
#     print(a*b)

# perkalian(2,3)

# x = lambda a,b: a*b
# print(x(2,3))

# y = lambda a,b,c: (a/b)*c
# print(y(1,2,3))

# z = lambda a: 'Genap' if a%2==0 else 'Ganjil'
# print(z(4))
# print(z(3))

# ## MAP ##
# name_list = 'Andi Boedi Caca'.split()

# def function(a):
#     return len(a)

# len_list = list(map(function, name_list))
# print(len_list)

# len_list2 = list(map(lambda a: len(a), name_list))
# print(len_list2)

# list_1 = 'cokelat melon nangka'.split()
# list_2 = [10000, 5000, 20000]
# couple_list = list(map(lambda  a, b: a + str(b), list_1, list_2))
# print(couple_list)

# ## FILTER ##
# h = range(11)
# def kurang_lima(x):
#     if x < 5:
#         return True
#     else:
#         return False

# j = list(filter(kurang_lima, h))

# print(j)
# print(list(h))

# k = [1,2,3,4,5]
# l = [1,2,6,7,8]

# m = list(filter(lambda a: a not in k, l))
# print(m)

# ### LATIHAN ###
# # map dan lambda #
# '''
# input = [2,4,6,8]
# output = [4,16,36,64] '''

# input_angka = [2,4,6,8]
# a = list(map(lambda a: a**2, input_angka))
# print(a)


# ''' kuis
# word_list = [merdeka, hello, sohib, kari ayam, pesawat, mobil, loker, kamar, saya, motor, pertamax, merah]
# what do you want to search: 'me'
# output = ['merdeka', 'merah']

# '''
# # word_list = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']
# # inputnya = str(input('mau cari apa: '))
# # hasil = filter(lambda a: inputnya in a, word_list)
# # print(list(hasil))


# ## REDUCE ##
# from functools import reduce

# number = [6,2,3,4,5]
# number_sum = reduce(lambda a,b: a+b, number)
# print(number_sum)

# number = [6,2,3,4,5]
# number_sum = reduce(lambda a,b: a*b, number)
# print(number_sum)

# kata = ['ini ', 'ibu ', 'budi']
# o = reduce(lambda a,b: a+b, kata)
# print(o)



''' kuis
input = [1-100]

output = 5100

[1,2,3,4]
[2,4]
[4,8]
12
rules = bilangannya genap semua, dikalikan 2, baru dijumlah semua.
challange = kalo bisa cuma 1 line
challange = pakai reduce, filter dan map
'''


a = 'andi budi caca'.split()
print(list(enumerate(a, 0)))

# x = 5
# y = '5'
# z = 6

# #conditional statement
# print(x == float(y))
# print(x == z)

'''
imt = ((massa / tinggi)/tinggi)*1000
< 18.5
berat badan anda kurang
18.5 - 24.9
berat badan anda ideal
25 - 29.9
berat badan berlebih
30 - 39.9
sangat berlebih
40 <
anda obesitas
Massa anda 60 kg dan tinggi anda 1.7 m
'''

berat = int(input('Masukkan berat badan:'))
tinggi = int(input('Masukkan tinggi badan:'))
imt = ((berat / tinggi)/tinggi)*1000
print(f"{imt} Berat badan {berat} kg dan Tinggi {tinggi/100} m")

if imt < 18.5:
    print('Berat badan kurang')
elif imt >= 18.5 and imt <= 24.9:
    print('Berat badan ideal')
elif imt >= 25 and imt <= 29.9:
    print('Berat badan lebih')
elif imt >= 30 and imt <= 39.9:
    print('Berat badan sangan berlebihan')
else:
    print ('obesitas')



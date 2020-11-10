# f(x) = 2x + 3
# f(3) = 2(3) + 3
# f(3) = 9

# function hello world
# def hello():
#     print("Hello World!")

# hello()

# # function pangkat 2
# def power():
#     print(3**2)

# power()

# def power2(x):
#     print('print dari dalam function', x**2)
#     return(x**2)

# hasil_power = power2(4)
# print('print dari luar function', hasil_power)

# # fuction 2 parameter
# def power3(angka, pangkat):
#     return angka**pangkat

# hasil_power3 = power3(3, 4)
# # print(power3(3, 4))
# print('di print dari variable hasil_power3:', hasil_power3)

'''







'''

# angka1 = input('angka pertama: ')
# oper = input('Operator(+,-,x,/,^): ')
# angka2 = input('angka kedua: ')

# def calculator(x1, op, x2):
#     if (x1.isnumeric() == True) and (op.isascii() == True) and (x2.isnumeric() == True):
#         x1 = int(x1)
#         x2 = int(x2)
#         if op == '+':
#             print(f'Hasil penjumlahan dari {x1} {op} {x2} adalah {x1+x2}')
#         elif op == '-':
#             print(f'Hasil pengurangan dari {x1} {op} {x2} adalah {x1-x2}')
#         elif op == 'x':
#             print(f'Hasil pengalian dari {x1} {op} {x2} adalah {x1*x2}')
#         elif op == '/':
#             print(f'Hasil pembagian dari {x1} {op} {x2} adalah {x1/x2}')
#         elif op == '^':
#             print(f'Hasil pemangkatan dari {x1} {op} {x2} adalah {x1**x2}')
#         else:
#             print(f'Operator {op} tidak ditemukan')
#     else:
#         print('Invalid Input')

# calculator(angka1, oper, angka2)


# 
angka1 = input('angka pertama: ')
oper = input('Operator(+,-,x,/,^): ')
angka2 = input('angka kedua: ')

def penjumlahan(y1, y2):
    return y1 + y2

def calculator(x1, op, x2):
    if (x1.isnumeric() == True) and (op.isascii() == True) and (x2.isnumeric() == True):
        x1 = int(x1)
        x2 = int(x2)
        if op == '+':
            print(f'Hasil penjumlahan dari {x1} {op} {x2} adalah {penjumlahan(x1, x2)}')
        elif op == '-':
            print(f'Hasil pengurangan dari {x1} {op} {x2} adalah {x1-x2}')
        elif op == 'x':
            print(f'Hasil pengalian dari {x1} {op} {x2} adalah {x1*x2}')
        elif op == '/':
            print(f'Hasil pembagian dari {x1} {op} {x2} adalah {x1/x2}')
        elif op == '^':
            print(f'Hasil pemangkatan dari {x1} {op} {x2} adalah {x1**x2}')
        else:
            print(f'Operator {op} tidak ditemukan')
    else:
        print('Invalid Input')

penjumlahan(angka1, oper, angka2)




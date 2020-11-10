# While Loops & For Loops
# Hanya akan menjalankan code ketika kondisinya True

# print(1*2)
# print(2*2)
# print(3*2)
# print(4*2)
# print(5*2)
# print(6*2)
# print(7*2)
# print(8*2)
# print(9*2)
# print(10*2)

# i = 1
# while i <= 20:
#     print(i*2)
#     i +=1

# i = 1
# while i <= 10:
#     i +=1
#     if i <= 5:
#         print(i*2)
#     else:
#         print(i*3)

# i = 1
# while i <= 20:
#     if i%2 == 0:
#         print('genap')
#     else:
#         print(i)
#     i += 1








'''
No. 1
password = '12345'

case 1:
input = 23452
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 23423
'Try again later'

case 2:
input 12345
'Password Correct'

case 3:
input = 23452
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 12345
'Password Correct'
'''

# passwprd = '12345'
# attempt = 1
# while attempt <= 4:
#     input_password = input('Ketik Password: ')
#     if input_password == password"
#         print('password correct')
#         break
#     else:
#         if attempt == 4:
#             print('try again later!')
#             break
#         else:
#             if attempt == 3:
#                 print(f'password incorrecr! you have {4=attempt} atttempt left!')
#             else:
#                 print(f'password incorrecr! you have {4=attempt} atttempt left!')
#                 attempt +=1


# def factorial(n):
#     result = 1

#     if n < 0 :
#         return 'Must be positive int'
#     else:
#         i = 1
#         while i <= n:
#             result *= i
#             i += 1
#     return result

# n = int(input('Masukkan n : '))
# print(factorial(n))




# def replace_0(kalimat):
#     kalimat = kalimat.replace('a', 'o')
#     kalimat = kalimat.replace('i', 'o')
#     kalimat = kalimat.replace('u', 'o')
#     kalimat = kalimat.replace('e', 'o')
#     return kamilat

# print

# def factorial(n): # n = 5
#     if n == 0: # 5 == 0 false
#         return 1
#     elif n == 1: # 5 == 1 false
#         return 1
#     elif n < 0: # 5 < 0 false
#         return 'must be positive digit'
#     else:   
#         result = 1
#         i = n
#         while i != 1:
#             result *=i -= 1
#             i -= 1
#         return result

# print(factorial(10))



# ################## FOR LOOP

# i = 1
# while i <= 10:
#     print(i*2)
#     i+=1

# for i in range(1,10):
#     if i == 5:
#         continue
#     else:
#         print(i*2)
## FOR Loops ##
# i = 1
# while i <= 10:
#     print(i*2)
#     i+=1

# for i in range(1,11):
#     print(i*2)

# for i in range(1,11):
#     if i == 5:
#         break
#     else:
#         print(i*2)

# for i in range(1,11):
#     if i == 5:
#         continue
#     else:
#         print(i*2)

# for i in range(6): # 0,1,2,3,4,5
#     print('*')

# for i in list(range(1,5)):
#     print(i)

# a_list = ['Budi', 'Andi', 'Candi', 'Dedi', 'Edi']
# b_list = ['Kapiten', 'Data Scientist', 'Tour Guide', 'Montir', 'Reparasi AC']
# for i in range(len(a_list)): # range(5) => 0,1,2,3,4
#     print(f'Halo nama saya {a_list[i]}! Pekerjaan Saya adalah {b_list[i]}')

# a_list = ['Budi', 'Andi', 'Candi', 'Dedi', 'Edi']
# b_list = ['Kapiten', 'Data Scientist', 'Tour Guide', 'Montir', 'Reparasi AC']
# for i, j in zip(a_list, b_list): # range(5) => 0,1,2,3,4
#     print(f'Halo nama saya {i}! Pekerjaan Saya adalah {j}')

# case 2

'''
# for i in range(1,10):
#     if i == 5:
#         continue
#     else:
#         print(i*2)



# case 1

''buat sebuah function untuk game fizz buzz!
function ini menerima 1 parameter.
ketika bertemu angka yang habis dibagi 3 maka dia akan print fizz [3,6,9,12]
ketika bertemu angka yang habis dibagi 5 maka dia akan print buzz [5,10,15,20,25]
ketika bertemu angka yang habis dibagi 3 dan 5 maka dia akan print fizz buzz [15, 30, 45]'''

# angka = int(input('Masukkan Angka : '))

# def fizzbuzz(a):
#     for i in range(1,a+1):
#         if i % 5 == 0 and i % 3 == 0:
#              print('fizzbuzzz')
#         elif i % 5 == 0:
#              print('fizz')
#         else i % 3 == 0:
#              print('buzz')   
#         print(i)
        

                


# for i in range (1,15+1): # atuu gini 1,+=1

#     if i % 3 == 0 and i % 5 == 0:
#         print('FIZZBUZZ')
#     elif i % 5 == 0:
#         print('BUZZ')
#     elif i % 3 == 0:
#         print('FIZZ')
#     else:
#         print(i)

# for i in range (1,15+1): # atuu gini 1,+=1

#     if i % 15 == 0:
#         print('FIZZBUZZ')
#     elif i % 5 == 0:
#         print('BUZZ')
#     elif i % 3 == 0:
#         print('FIZZ')
#     else:
#         print(i)        

# for i in range (1,20):

#     if i % 3 == 0: 
#         print('FIZZ')
#     elif i % 5 == 0:
#         print('BUZZ')
#     elif i % 3 == 0 and i % 5 == 0:
#         print('FIZZBUZZ')
#     else:
#         print(i)        

# case 2
'''case 2
tanpa membuat function, buatlah sebuah program untuk reversing namun menggunakan for loop
input = [1,2,3,4,5,6,7]

output = [7,6,5,4,3,2,1]'''
# inp = 1,2,3,4,5,6,7
# output = []
# a = 0
# for i in range(0,len(inp)):
#         a -=1
#         output.append(inp[a])
#         print(output)

# case 3

# kata = 'owowowow'
# len_kata = len(kata)
# is_palindrome = False
# for i in range(0, len_kata):
#      if kata[i] == kata[-i-1]:
#           is_palindrome = True
#      else:
#           is_palindrome = False
#           break
# print(f"Is word {kata.upper()} is Palindrome? {is_palindrome}")




















# def cekkata():
#     kata = input('Masukkan kata: ').lower()
#     list2 = '' #l
#     # k = 0
#     for i in range(len(kata)): # 0
#         # k -= 1 # k = -2; k = -
#         #             -(1+1)
#         list2 += kata[-(i+1)] # list2 = lib --> libom
#     if list2 == kata:
#         print(f'{kata} is a palindrome')
#     else: print(f'{kata} is not a palindrome')

# cekkata()


# # case 4

# baris = int(input("segitika_siku "))
# angka = baris
# for i in range(1, baris + 1):
#     for ii in range(1, baris + 1):
#         if(i < ii):
#             print(' ', end = ' ')
#         else:
#             print('angka', end = ' ')
#     print()

# baris = int(input("segitika_siku "))
# for i in range(1, baris + 1):
#     for ii in range(1, i + 1):
#      #    if(i < ii):
#             print(ii, end = ' ')
#      #    else:
#      #        print(' ', end = ' ')
#     print("")





    
# # case 5

baris = int(input("segitika_siku "))
for i in range(0, baris + 1):
    for ii in range(0, baris + 1):
        if(i > ii):
            print('* ', end = ' ')
        else:
            print(' ', end = ' ')
    print()

# def segitiga_siku(x):
#      star = ''
#      for i in range(x):
#           star += ' * '
#           print(star)

# segitiga_siku(5)

# List comprehesion
# z_list = [1,2,3,4,5]
# a_list = [i*2 for i in z_list]

# # slicing dictionary with loop
# a_dict = {
#      'nama': 'Andi',
#      'kelas': '1C',
#      'status': 'Jomlo',
#      'penghasilan': 'Belum punya'
#      }
# slice_list = 'nama penghasilan'.split()
# slice_dict = {i: a_dict[i] for i in slice_list}
# print(slice_dict)
# print(a_list)

# def pattern(n):
#       k = 2*n-2
#       for i in reversed(range(0, n)):#for i in range(n,-1,-1):
#            for j in range(0,k):
#                 print(end=" ")
#            k = k + 1
#            for j in range(0, i+1):
#                 print("*", end=" ")
#            print(" ")
#       k = 2*n-2
#       for i in range(0,n):
#            for j in range(0,k):
#                print(end=" ")
#            k = k - 1
#            for j in range(0, i+1):
#                 print("*", end=" ")
#            print(" ")
# pattern(5)

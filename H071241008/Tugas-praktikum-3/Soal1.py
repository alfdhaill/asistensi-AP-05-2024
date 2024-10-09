import os
os.system('cls')
tinggi_2pac = int(input('Masukkan tinggi baris: '))
panjang = 1
n = tinggi_2pac - 1
for i in range(tinggi_2pac // 2):
    print(f'{" "*n}{"* "*panjang}')
    panjang += 2
    n -= 2
if tinggi_2pac % 2 == 1:
    print(f'{" "*n}{"* "*panjang}')
for i in range(tinggi_2pac // 2):
    panjang -= 2
    n += 2
    print(f'{" "*n}{"* "*panjang}')

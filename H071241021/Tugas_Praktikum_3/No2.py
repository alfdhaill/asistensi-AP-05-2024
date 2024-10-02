import random

angka_acak = random.randint (1, 100)
percobaan = 1 
maks_percobaan = 6

while percobaan < maks_percobaan:
    try:
        tebakan = int(input (f'Percobaan {percobaan} : Masukkan tebakan anda (0 untuk berhenti): '))
    except ValueError:
        print('Masukkan angka yang valid')
        continue
    if tebakan == 0:
        print('Permainan Dihentikan')
        break
    
    percobaan += 1

    if tebakan == angka_acak:
        print('Selamat! anda menebak angka dengan benar')
        break
    elif tebakan < angka_acak:
        print('Angka terlalu kecil')
    else:
        print ('Angka terlalu besar')

    if percobaan == maks_percobaan:
        print ('Percobaan Habis')
        print (f'Angka yang benar adalah {angka_acak}')


















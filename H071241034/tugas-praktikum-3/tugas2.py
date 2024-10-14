import random
angka_rahasia = random.randint (1,100)
percobaan = 0 
batas_percobaan = 5 

while percobaan <5 :
    tebakan = int(input("masukkan angka(0untuk berhenti)"))

    if tebakan == 0 :
       print('permainan dihentikan')
       break
    percobaan += 1

    if tebakan > angka_rahasia :
        print('angka terlalu besar')

    elif tebakan < angka_rahasia :
        print("angka terlalu kecil") 
    else :
        print("benar anda menang")
        break
    if percobaan == 5 and tebakan != angka_rahasia :
        print(f"anda kalah angka yang benar {angka_rahasia}")   


import random 
 
angka_rahasia = random.randint(1, 100) 
percobaan_max = 5
percobaan = 0 

while percobaan < percobaan_max:
    angka=input("masukkan angka = ")
    percobaan += 1
    try :
        angka= int(angka)
    except :
        print("Harus memasukkan angka") 
        continue
    if angka > angka_rahasia :
        print('Tebakan angka terlalu besar')
    elif angka < angka_rahasia :
        print('tebakan angka terlalu kecil')
    else :
        print(f"tebakan anda benar, yaitu{angka_rahasia}")
        
    if percobaan > 5: 
        print(f"Maaf, Anda gagal menebak angka rahasia. Angka rahasia adalah {angka_rahasia}.")
        break
    print(percobaan)

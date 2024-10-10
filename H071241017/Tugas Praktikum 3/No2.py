import random
# buat angka random dari 1 and 100
angka_rahasia = random.randint(1, 100)
percobaan = 0
batas_percobaan = 5

print("Ketik '0' jika Anda ingin menghentikan permainan kapan saja.")

while percobaan < batas_percobaan:
    tebakan = int(input("Masukkan tebakan Anda: "))
    
    if tebakan == 0:
        print("Permainan dihentikan. Terima kasih telah bermain!") 
        break
    
    percobaan += 1
    
    if tebakan == angka_rahasia:
        print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dengan benar")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")
    
    if percobaan == batas_percobaan:
        print(f"Maaf, Anda telah mencapai batas maksimal {batas_percobaan} percobaan. Angka yang benar adalah {angka_rahasia}.") 
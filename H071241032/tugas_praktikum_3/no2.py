import random

angka_rahasia = random.randint(1, 100)
percobaan = 5

print("Permainan menebak angka dimulai!")
print("Tebak angka antara 1 hingga 100. Anda memiliki 5 kesempatan. Ketik '0' untuk berhenti.")

for i in range(percobaan):
    tebakan = int(input(f"Percobaan {i+1}: Masukkan tebakan Anda: "))
    
    if tebakan == 0 :
        print("Permainan dihentikan. Terima kasih telah bermain!")
        break
    
    if tebakan == angka_rahasia:
        print("Selamat! Tebakan Anda benar.")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")

if tebakan != angka_rahasia and tebakan != 0:
    print(f"Maaf, Anda kehabisan kesempatan. Angka rahasia adalah {angka_rahasia}.")

import random

angka_rahasia = random.randint(1, 100)

maksimal_percobaan = 5
percobaan = 0

while percobaan < maksimal_percobaan:
    tebak = int(input(f"Masukkan Tebakan anda (0 untuk berhenti) : "))
    
    if tebak == 0:
        print("Kamu telah menyerah. Permainan berakhir.")
        break
    
    if tebak == angka_rahasia:
        print(f"Selamat! Anda menebak dengan angka benar.")
        break

    elif tebak > angka_rahasia:
        print("Angka terlalu besar.")

    else:
        print("Angka terlalu kecil.")
    
    percobaan += 1


if percobaan == maksimal_percobaan and tebak != angka_rahasia:
    print(f"Kesempatan habis! Angka rahasia adalah {angka_rahasia}.")

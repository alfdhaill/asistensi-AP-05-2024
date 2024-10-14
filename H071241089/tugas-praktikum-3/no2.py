import random

angkaRandom = random.randint(1, 100)

for i in range(5):
    try:
        angkaTebakan = int(
            input("Masukkan tebakan Anda (0 untuk berhenti) : "))
        if angkaTebakan == 0:
            break
        elif angkaTebakan > angkaRandom:
            print("Angka terlalu besar.")
        elif angkaTebakan < angkaRandom:
            print("Angka terlalu kecil.")
        else:
            print("Selamat! Anda menebak angka dengan benar.")
            break
    except ValueError:
        print("Mohon masukkan Angka.")

print("Angka yang benar adalah :", angkaRandom)

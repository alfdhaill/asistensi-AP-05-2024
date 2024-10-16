import random

secret_number = random.randint(1,100)

print("Selamat datang di permainan tebak angka!")
print("Saya telah memilih angka antara 1 hingga 100.")
print("Anda memiliki maksimal 5 kali percobaan untuk menebak angka.")
print("Ketik '0' untuk keluar dari permainan.")

for attempts in range(1,6):
    print(f"\n Percobaan ke-{attempts}")
    
    try:
        guess = int(input("Masukkan tebakan Anda (0 untuk berhenti) : "))
        if guess == 0:
            print("Anda telah keluar dari permainan.")
            break
        elif guess < 0:
            print("Angka tidak boleh dibawah 0")
        elif guess > 100:
            print("Angka tidak boleh diatas 100")
        elif guess == secret_number:
            print(f"Selamat! Anda berhasil menebak angka yang benar adalah {secret_number}.")
            break
        elif guess < secret_number:
            print("Angka terlalu kecil.")
        else:
            print("Angka terlalu besar.")
        
        if attempts == 5:
            print(f"Permainan selesai! Angka yang benar adalah {secret_number}.")
    except:
        print("Harap memasukkan sebuah angka")
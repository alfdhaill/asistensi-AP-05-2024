import random
secret_number = random.randint(1,100)

print ('SELAMAT DATANG DI PERMAINAN TEBAK ANGKA 1-100')
print ('SAYA SUDAH MEMILIKI ANGKA ANTARA 1 - 100')
print ('KAMU MEMILIKI KESEMPATAN SEBANYAK 5 KALI UNTUK MENEBAK ')
print ("Ketik '0' untuk keluar dari permainan.")

for x in range (1,6):
    try:
        print (f'percobaan ke-{x}')
        guess = int (input("MASUKKAN ANGKA TEBAKAN: "))
        if guess == 0 :
            print ('GAME TELAH SELESAI ')
            break 
        elif guess > 100 : 
            print ('ANGKA TIDKA BOLEH LEBIH DARI 100')
        elif guess < 0 :
            print ('ANGKA TIDAK BOLEH KURANG DARI 0')
        elif guess == secret_number:
            print ('SELAMAT KAMU MENEBAK ANGKA YANG BENAR ')
        elif guess < secret_number:
            print ('ANGKA LEBIH BESAR')
        else:
            print ('ANGKA LEBIH KECIL')
        if x == 5 :
            print (F'PERMAINAN SELESAI, ANGKA YANG BENAR ADALAH {secret_number}')
        
    except:
        print ('HARAP MASUKKAN SEBUAH ANGKA')
        

        

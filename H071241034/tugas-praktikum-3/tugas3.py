N =int(input("masukkan angka N : "))  #baris
M = int(input("masukkan angka M : ")) #kolom

for row in range(N):
    if row % 2 == 0:
        for col in range(M):
            print("MOVE to ({row},{col})")
    else:
        # Jika baris ganjil, gerak ke kiri
        for col in range(M-1, -1, -1):
            print("MOVE to ({row},{col})")
# pelajari import random

    
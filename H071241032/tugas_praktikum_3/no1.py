n = int(input("Masukkan jumlah baris: "))

if n == 0:
    print("Angka harus lebih dari nol bro")

else:
    mid = n // 2
    for i in range(mid + (n % 2)):
         print(" " * (mid - i) + "*" * (2 * i + 1))
    
    for i in range(mid  - 1, -1, -1):
         print(" " * (mid - i) + "*" * (2 * i + 1))
          
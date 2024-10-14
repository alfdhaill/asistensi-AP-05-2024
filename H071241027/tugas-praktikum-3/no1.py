n = int(input("Masukkan jumlah baris untuk belah ketupat: "))

if n % 2 == 0:
    for i in range(1, n, 2):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -2):
        print(" " * (n - i) + "* " * i)
else :
    for i in range(1, n, 2):
        print(" " * (n - i) + "* " * i)
    for i in range(n, 0, -2):
        print(" " * (n - i) + "* " * i)
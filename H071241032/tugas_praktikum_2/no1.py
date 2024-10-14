a = int(input("Masukkan panjang sisi pertama: "))
b = int(input("Masukkan panjang sisi kedua: "))
c = int(input("Masukkan panjang sisi ketiga: "))
if (a + b > c) and (b + c > a) and (a + c > b):
    if a == b == c:
        print("Segitiga Sama Sisi")
    elif a != b == c or a == b != c or a == c != b:
        print("Segitiga Sama Kaki") 
    else:
        print("Segitiga Sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")
    
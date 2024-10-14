sisiA = int(input("Masukkan panjang sisi pertama : "))
sisiB = int(input("Masukkan panjang sisi kedua : "))
sisiC = int(input("Masukkan panjang sisi ketiga : "))

if sisiA + sisiB > sisiC and sisiB + sisiC > sisiA and sisiC + sisiA > sisiB:
    if sisiA == sisiB == sisiC:
        print("Segitiga sama sisi")
    elif sisiA == sisiB or sisiB == sisiC or sisiA == sisiC:
        print("Segitiga sama kaki")
    else:
        print("Segitiga sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")

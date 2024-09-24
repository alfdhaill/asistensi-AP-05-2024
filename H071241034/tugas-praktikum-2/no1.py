sisi1 = float(input("Masukkan panjang sisi pertama : "))
sisi2 = float(input("Masukkan panjang sisi kedua: "))
sisi3 = float(input("Masukkan panjang sisi ketiga: "))

if sisi1 + sisi2 > sisi3 and sisi1 + sisi3 > sisi2 and sisi2 + sisi3 > sisi1:
    if sisi1 == sisi2 == sisi3:
        print("Segitiga sama sisi")
    elif sisi1  == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
        print("Segitiga sama kaki")
    else:
        print("Segitiga sembarang")
else:
    print(" tidak dapat membentuk segitiga yang valid")

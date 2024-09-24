sisi1 = int(input("Masukkan panjang sisi pertama : "))
sisi2 = int(input("Masukkan panjang sisi kedua : "))
sisi3 = int(input("Masukkan panjang sisi ketiga : "))

if sisi1 + sisi2 > sisi3 and sisi1 + sisi3 > sisi2 and sisi2 + sisi3 > sisi1 :

    if sisi1 == sisi2 == sisi3 :
        print("Segitiga sama sisi")
        
    elif sisi1 == sisi2 != sisi3 :
        print("Segitiga sama kaki")
        
    elif sisi1 != sisi2 == sisi3:
        print("Segitiga sama kaki")
        
    elif sisi1 == sisi3 != sisi2:
        print("Segitiga sama kaki")
        
    elif sisi1 != sisi2 != sisi3:
        print("Segitiga sembarang")
     
else :
    print("Tidak dapat membentuk segitiga yang valid")
    

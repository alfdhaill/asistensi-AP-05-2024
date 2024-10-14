usia = int(input("Masukkan usia anda : "))
anggota = input("Apakah anda anggota? (ya/tidak) : ")

if usia < 5 :
    print("Harga tiket : Gratis")
    harga_akhir = 0

else :
    
    if 5 <= usia <= 12:
        harga_tiket = 50000
    elif 13 <= usia <= 59:
        harga_tiket = 100,000
    elif usia >= 60 :
        harga_tiket = 70000
        
    harga_akhir = harga_tiket * 0.8 if anggota =='ya' else harga_tiket
    

print(f"Harga tiket yang harus dibayar : Rp {int(harga_akhir)}")
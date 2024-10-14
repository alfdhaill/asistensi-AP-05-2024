usia = int(input("Masukkan usia: "))
x = input("Apakah Anda anggota (ya/tidak): ")

if usia < 5:
     harga = "Gratis" 
elif 5 <= usia <= 12:
    harga = 50000 
elif 13 <= usia <= 59:
    harga = 100000   
elif usia >= 60:
    harga = 70000
hasil = harga * 0.8 if x == "ya" and harga != "Gratis" else harga
if harga == "Gratis":
    print("Harga tiket: Rp.0 atau Gratis")
else:
    print("Harga tiket: Rp.",int(hasil))

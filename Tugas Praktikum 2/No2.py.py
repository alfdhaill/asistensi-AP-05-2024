#soal 2
usia = int(input("masukan usia anda : "))
anggota = input("apakah anda anggota (ya/tidak) : ")

if usia < 5:
    harga_tiket = 0
elif usia>=5 and usia<=12:
    harga_tiket = 50000
elif usia>=13 and usia<=59:
    harga_tiket = 100000
else: #usia > 60
    harga_tiket = 70000

if anggota == 'ya' :
     harga_tiket *= 0.8  # Diskon 20%

print(f"harga tiket : Rp. {int(harga_tiket)}") 
    
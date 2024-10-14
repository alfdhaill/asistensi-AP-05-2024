usia = int(input('Masukkan usia : '))
anggota = input("Apakah Anda anggota (ya/tidak) : ")

if usia < 5:
    hargaAwal = 0
if 5 <= usia <= 12:
    hargaAwal = 50000
elif 13 <= usia <= 59:
    hargaAwal = 100000
elif usia >= 60:
    hargaAwal = 70000

harga = hargaAwal - ((hargaAwal * 20) // 100
                     ) if anggota == "ya" else hargaAwal

print(f"Harga tiket : Rp. {harga}")

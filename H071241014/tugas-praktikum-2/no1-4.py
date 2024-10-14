#JAWABAN SOAL 1
#Program Segitiga

sisi1 = (input("Masukkan panjang sisi pertama: "))
sisi2 = (input("Masukkan panjang sisi kedua: "))
sisi3 = (input("Masukkan panjang sisi ketiga: "))

if sisi1 + sisi2 <= sisi3 or sisi1 + sisi3 <= sisi2 or sisi2 + sisi3 <= sisi1 or sisi1 == sisi2 == sisi3 == 0:
    print("Tidak dapat membentuk segitiga yang valid")
elif sisi1 == sisi2 == sisi3:
    print("Segitiga Sama Sisi")
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print("Segitiga Sama Kaki")
else:
    print("Segitiga Sembarang")

#JAWABAN SOAL 2

#Program Tiket Wahana

usia = int(input("Masukkan Usia: "))

if usia < 5:
    harga = 0
elif 5 <= usia <= 12:
    harga = 50000
elif 13 <= usia <= 59:
    harga = 100000
else:
    harga = 70000

keanggotaan = input("Apakah Anda Anggota? (ya/tidak): ")

diskon = harga - (harga * 20/100)

harga_tiket = diskon if keanggotaan == "ya" else harga

print(f'Harga Tiket: Rp{harga_tiket:.0f}')


#JAWABAN SOAL 3
#Program Kelulusan

nilai = int(input("Masukkan Nilai Akhir: "))
kehadiran = int(input("Masukkan Persentase Kehadiran: "))

if 85 <= nilai <= 100 and kehadiran >= 75:
    print("Lulus dengan Predikat A")
elif 70 <= nilai <= 84 and kehadiran >= 75:
    print("Lulus dengan Predikat B")
elif 60 <= nilai <= 69 and kehadiran >= 75:
    print("Lulus dengan Predikat C")
elif nilai < 60 and kehadiran >= 75:
    tugas_tambahan = int(input("Masukkan Nilai Tugas Tambahan: "))
    if tugas_tambahan > 70 and kehadiran >= 75:

        print("Lulus dengan Predikat C")
else:
    print("Tidak Lulus")

#JAWABAN SOAL 4

#Program Paket Internet

jumlah_data = int(input("Masukkan jumlah data yang Anda gunakan: "))
penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ")
personal_bisnis = input("Apakah Anda pengguna Personal atau Bisnis? ")

if jumlah_data < 10 and penggunaan == "off-peak" and personal_bisnis == "personal":
    print("Paket yang Sesuai: Paket A")
elif 10 <= jumlah_data <= 50 and penggunaan == "peak" and personal_bisnis == "personal":
    print("Paket yang Sesuai: Paket B")
elif jumlah_data > 50 and penggunaan == "peak" and personal_bisnis == "personal" == "bisnis":
    print("Paket yang Sesuai: Paket C")
elif jumlah_data > 50 and penggunaan == "off-peak" and personal_bisnis == "bisnis":
    print("Paket yang Sesuai: Paket D")
else:
    print("Tidak Ada Paket yang Cocok")
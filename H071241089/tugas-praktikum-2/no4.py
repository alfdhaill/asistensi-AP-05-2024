jumlahData = float(input("Masukkan Jumlah Data Yang Digunakan (GB) : "))
waktuPenggunaan = input(
    "Apakah Mayoritas Penggunaan Di Luar Jam Sibuk (off-peak) Atau Di Jam Sibuk (peak) ? ")
jenisPengguna = input("Apakah Anda Pengguna Personal Atau Bisnis ? ")

if jumlahData < 10:
    tipePenggunaanData = "ringan"
elif 10 <= jumlahData <= 50:
    tipePenggunaanData = "sedang"
else:
    tipePenggunaanData = "berat"

match (tipePenggunaanData, waktuPenggunaan, jenisPengguna):
    case ("ringan", "off-peak", "personal"):
        saran = "Paket A"
    case ("sedang", "peak", "personal"):
        saran = "Paket B"
    case ("berat", "peak", "personal") | ("berat", "peak", "bisnis"):
        saran = "Paket C"
    case ("berat", "off-peak", "bisnis"):
        saran = "Paket D"
    case _:
        saran = "Tidak Ada Paket Yang Cocok"

print(f"Paket Yang Sesuai: {saran}")

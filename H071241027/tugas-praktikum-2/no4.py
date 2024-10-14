data = float(input("Masukkan Jumlah Data Yang Digunakan (GB) : "))
jam = input("Apakah Mayoritas Penggunaan Di Luar Jam Sibuk (off-peak) Atau Di Jam Sibuk (peak) ? ")
jenis = input("Apakah Anda Pengguna Personal Atau Bisnis ? ")

if data < 10:
    kat_data = "ringan"
elif 10 <= data <= 50:
    kat_data = "sedang"
else:
    kat_data = "berat"

match (kat_data, jam, jenis):
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

print(f"Paket Yang Sesuai: {saran}")
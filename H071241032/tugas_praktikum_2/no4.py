penggunaan_data = int(input("Masukkan penggunaan data per bulan (GB): "))
waktu_penggunaan = input("Masukkan waktu penggunaan (off-peak/peak): ")
jenis_pengguna = input("Masukkan jenis pengguna (personal/bisnis): ")

if penggunaan_data < 10:
    kategori_data = "Ringan"
elif 10 <= penggunaan_data <= 50:
    kategori_data = "Sedang"
else:
    kategori_data = "Berat"

if kategori_data == "Ringan" and waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
    paket = "Paket A"
elif kategori_data == "Sedang" and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
    paket = "Paket B"
elif kategori_data == "Berat" and waktu_penggunaan == "peak":
    paket = "Paket C"
elif kategori_data == "Berat" and jenis_pengguna == "bisnis" and waktu_penggunaan == "off-peak":
    paket = "Paket D"
else:
    paket = "Tidak ada paket yang cocok"

print(f"Paket yang sesuai untuk Anda adalah: {paket}")
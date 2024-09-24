data = int(input("Masukkan jumlah data yang digunakan (GB):"))
waktu = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk(peak)?")
jenis = input("Apakah anda pengguna personal atau bisnis?")

if data <10 and waktu == "off-peak" and jenis == "personal" :
    paket = "A"
elif data >= 10 and data <= 50 and waktu == "peak" and jenis == "personal" :
    paket = "B"
elif data >50 and waktu == "peak" and waktu == "peak" and jenis ==  "personal" or 'bisnis':
    paket = "C"
elif data > 50 and waktu == "off-peak"  and jenis == "bisnis":
    paket = "D"

else :
    paket = ("Paket tidak ada yang cocok")

print (f"paket yang sesuai : {paket}")
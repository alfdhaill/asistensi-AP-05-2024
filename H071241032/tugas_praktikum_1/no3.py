print("Konversi detik ke jam")
detik = int(input("masukkan jumlah detik : "))
jam = detik // 3600
menit = (detik % 3600) // 60
detik = detik % 60
hasilnya =f"{jam}:{menit:02}:{detik:02}"
print(hasilnya)

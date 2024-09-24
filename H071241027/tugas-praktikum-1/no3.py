print("Konversi detik ke jam")
total_detik = int(input("Masukkan jumlah detik : "))

jam = total_detik // 3600
menit = (total_detik % 3600)// 60
detik = total_detik % 60

print(f"{jam:02d}:{menit:02d}:{detik:02d}")

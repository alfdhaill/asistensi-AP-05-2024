print("Konversi detik ke jam")
detikInp = int(input("Masukkan jumlah detik: "))

jam = ((detikInp - (detikInp % 3600)) // 3600)
menit = (detikInp % 3600 // 60)
detik = detikInp % 60

print(f"{jam:02}:{menit:02}:{detik:02}")

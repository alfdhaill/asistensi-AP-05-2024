print("## Program Konversi Detik ##")
print("===========================")
print()
print ("konversi detik ke jam")
jumlahdetik = int(input("Masukkan Detik : "))
jam = jumlahdetik // 3600
sisadetik = jumlahdetik % 3600
menit = sisadetik // 60
detik = sisadetik % 60
print(f"{jam}:{menit:02}:{detik:02}")
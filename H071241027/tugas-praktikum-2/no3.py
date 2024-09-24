nilai_akhir = int(input("Masukkan nilai akhir: "))
persentase = int(input("Masukkan persentase kehadiran: "))
tugas_tambahan = int(input("Masukan nilai tugas tambahan : "))

if nilai_akhir >= 85 and persentase >= 75:
    predikat = "A"
    print(f"Mahasiswa lulus dengan predikat {predikat}")
    
elif 70 <= nilai_akhir < 84 and persentase >= 75:
    predikat = "B"
    print(f"Mahasiswa lulus dengan predikat {predikat}")
    
elif 60 <= nilai_akhir < 70 and persentase >= 75:
    predikat = "C"
    print(f"Mahasiswa lulus dengan predikat {predikat}")
    
elif nilai_akhir < 60 and persentase >= 75 and tugas_tambahan > 70 :
    predikat = "C"
    print(f"Mahasiswa lulus dengan predikat {predikat}")
    
elif nilai_akhir < 60 and persentase >= 75:
    predikat = "Tidak Lulus"
    print(f"Mahasiswa {predikat}")
    
else:
    predikat = "Mahasiswa Tidak Lulus"
    

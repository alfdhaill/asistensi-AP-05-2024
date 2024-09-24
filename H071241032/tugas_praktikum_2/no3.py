nilai = int(input("Masukkan nilai akhir: "))
kehadiran = int(input("Masukkan Persentase kehadiran: "))
tugas_tambahan = int(input("Masukkan nilai tambahan: "))
if kehadiran < 75:
    hasil = "Tidak lulus "
elif nilai >= 85 :
    hasil= "Lulus dengan Predikat A"
elif nilai >= 70 :
    hasil = "Lulus dengan Predikat B"
elif nilai >= 60:
    hasil = "Lulus dengan Predikat C"
else:
    if tugas_tambahan > 70:
         hasil = "Lulus dengan Predikat C"
    else:
        hasil = "Tidak Lulus (Tugas tambahan tidak mencukupi)"

print(f"Hasil: {hasil}")
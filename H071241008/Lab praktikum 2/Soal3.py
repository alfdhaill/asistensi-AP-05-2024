nilai_akhir = int(input('masukkan nilai akhir: '))
kehadiran = int(input('masukkan kehadiran: '))
tugas_tambahan = int(input('masukkan nilai semua tugas tambahan: '))

if kehadiran < 75:
    print('tidak lulus (kehadiran kurang dari 75 %)')
elif nilai_akhir >= 85:
    print('Lulus dengan predikat A')
elif nilai_akhir >= 70:
    print('Lulus dengan predikat B')
elif nilai_akhir >= 60:
    print('Lulus dengan predikat C')
elif nilai_akhir <= 60 and tugas_tambahan > 70:
    print('Lulus dengan predikat C (berdasarkan tugas tambahan)')
else :
    print ('tidak lulus')
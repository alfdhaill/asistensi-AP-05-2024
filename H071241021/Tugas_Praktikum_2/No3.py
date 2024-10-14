NilaiAkhir = int(input('Masukkan Nilai Akhir : '))
Kehadiran = int(input('Masukkan Presentase Kehadiran : '))

if Kehadiran >= 75:
    if 85 <= NilaiAkhir <= 100:
        print ('Lulus Dengan Predikat A')
    elif 70 <= NilaiAkhir <= 84:
        print ('Lulus Dengan Predikat B')
    elif 60 <= NilaiAkhir <= 69:
        print ('Lulus Dengan Predikat C')      
    elif NilaiAkhir < 60:
        NilaiTambahan = int(input('Nilai Tugas Tambahan :'))
        if NilaiTambahan > 70 :
            print ('Lulus Dengan Predikat C')
        else :
            print ('Tidak Lulus')
        
else:
    print ('Tidak Lulus')




nilai_akhir = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))

if kehadiran < 75:
    print("Tidak Lulus karena kehadiran kurang dari 75%.")
else:
    if nilai_akhir >= 85:
        print("Lulus dengan Predikat A.")
    elif nilai_akhir >= 70:
        print("Lulus dengan Predikat B.")
    elif nilai_akhir >= 60:
        print("Lulus dengan Predikat C.")
    else:
        tugas_tambahan = input("Apakah tugas tambahan selesai dengan baik (ya/tidak)? ").lower()
        if tugas_tambahan == 'ya':
            print("Lulus dengan Predikat C (melalui tugas tambahan).")
        else:
            print("Tidak Lulus.")
 
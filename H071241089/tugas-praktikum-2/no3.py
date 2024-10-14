nilai = int(input("Masukkan nilai akhir : "))
kehadiran = int(input("Masukkan persentase kehadiran : "))

if kehadiran >= 75:
    if 85 <= nilai <= 100:
        kelulusan = "Lulus"
        predikat = "A"
    elif 70 <= nilai <= 84:
        kelulusan = "Lulus"
        predikat = "B"
    elif 60 <= nilai <= 69:
        kelulusan = "Lulus"
        predikat = "C"
    elif nilai < 60:
        tugasTambahan = int(input("Input nilai tugas tambahan : "))

        if tugasTambahan > 70:
            kelulusan = "Lulus"
            predikat = "C"
        else:
            kelulusan = "Tidak Lulus"
else:
    kelulusan = "Tidak Lulus"

print(f"{kelulusan} dengan Predikat {predikat}" if kelulusan ==
      "Lulus" else f"{kelulusan}")

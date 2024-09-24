# soal 3
nilai = float(input("masukan nilai akhir : "))
kehadiran = float(input("masukan prsentase kehadiran : "))
nt = int(input("Apakah anda mengerjakan tugas tambahan dengan baik? (ya : 1; tidak : 2) : "))

if kehadiran >= 75 :
    if nilai > 85 :
        print("lulus dengan predikat A")
    elif nilai > 70 and nilai < 84 :
        print("lulus dengan predikat B")
    elif nilai > 60 and nilai < 69 :
        print("lulus dengan predikat C")
    else:
        if nt == 1 :
            print("lulus dengan predikat C")
        elif nt == 2 :
            print("tidak lulus")
else:
    print("tidak lulus")


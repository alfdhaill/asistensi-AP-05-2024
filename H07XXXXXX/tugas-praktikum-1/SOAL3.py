
#SOAL 3
nilai = int (input(' masukkan nilai akhir :' ))
kehadiran = int (input ( "masukkan persantase kehadiran :"))
tugas_tambahan = int (input("masukan nilai tugas tambahan :"))

if kehadiran >= 75 :
  if nilai >= 85 :
    print ("Lulus dengan predikat A")
  elif  nilai >= 70 and nilai <= 84 :
    print ('Lulus dengan predikat B ')
  elif  nilai >= 60 and nilai <= 69 :
    print ("Lulus dengan prdedikat C ")
  elif tugas_tambahan >70 :
    print ( " Lulus dnegan predikat C")
  else :
    print (' tidak lulus ')
else :
  print (' tidak Lulus ')

#SOAL 2
x = int(input('masukan usia :'))
y = input( "apakah anda anggota (ya/tidak):")

if x < 5 :
    harga = 0
elif x>=5 and x<=12 :
    harga =50000
elif x>= 13 and x<= 59 :
    harga =100000
else :
    harga =70000

if y == 'ya' :
  harga = harga - (( harga * 20)//100)

print (f"harga tiket : Rp. {(harga)}")








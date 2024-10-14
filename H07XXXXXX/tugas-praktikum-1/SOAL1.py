#SOAL 1
x = float(input( "masukkan panjang sisi pertama :"))
y = float(input( "masukkan panjang sisi kedua :"))
z = float(input( "masukkan panjang sisi terakhir :"))

if x + y > z and y+z > x and z+x > y :

  if x==y==z :
   segitiga = 'segitiga sama sisi'
  elif x==z or x==y or y==z :
    segitiga = 'segitiga sama kaki'
  else :
    segitiga = 'segitiga sembarang'
else :
  segitiga = ("tidak dapat membentuk segitiga yang valid")



print(segitiga)
#SOAL 4
x = int(input(' masukkan jumlah data yang digunakan(GB):')) #penggunaan data
y = input ('apakah mayoritas pengunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak) ?') #waktu pengunaan
z = input (' apakah anda pengguna personal atau bisnis ?') #jenis pengguna

if x < 10 and y == "off-peak" and z == "personal" :
  print("paket yang sesuai : paket A") 
elif  10<= x <= 50 and y=='peak' and z == 'personal':
  print("paket yang sesuai : paket B") 
elif x > 50 and y== "peak" and  z== ['personal','bisnis'] :
  print("paket yang sesuai : paket C") 
elif x > 50 and y== "off-peak" and z== "bisnis" :
   print("paket yang sesuai : paket D") 
else :
  print ( "tidak ada paket yang cocok")







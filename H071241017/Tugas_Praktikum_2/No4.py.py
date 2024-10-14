#SOAL 4
data = int(input(' masukkan jumlah data yang digunakan(GB)? ')) 
waktu = input ('apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau pada jam sibuk (peak) ? ')
jenis = input (' apakah anda pengguna personal atau bisnis ? ')

if data < 10 and waktu == "off-peak" and jenis == "personal" :
  paket = "A"
elif  10<= data <= 50 and waktu =='peak' and jenis == 'personal':
  paket = "B"
elif data > 50 and waktu == "peak" and  jenis == ['personal','bisnis'] :
  paket = "C"
elif data > 50 and waktu == "off-peak" and jenis == "bisnis" :
  paket = "D"
else :
  paket = "data tidak valid"

print (f' paket yang sesuai : paket {paket}')

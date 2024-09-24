penggunaanData = int(input('masukkan jumlah data yang digunakan (gb): '))
waktuPenggunaan = input('apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk atau di jam sibuk (peak): ')
paket_layanan_yang_ditawarkan = input('apakah anda pengguna personal atau bisnis?: ')

if penggunaanData < 10 and waktuPenggunaan =='off-peak' and paket_layanan_yang_ditawarkan == "personal":
    paket = "paket A"

elif 10 <= penggunaanData <= 50 and waktuPenggunaan == 'peak' and paket_layanan_yang_ditawarkan == "personal":
    paket = "paket B"
   
elif penggunaanData > 50 and waktuPenggunaan == "peak" and (paket_layanan_yang_ditawarkan == "personal" or paket_layanan_yang_ditawarkan == "bisnis"):
    paket = "paket c"
  
elif penggunaanData > 50 and waktuPenggunaan =='off-peak' and paket_layanan_yang_ditawarkan =="bisnis":
    paket = "paket D"
   
else:
    paket = 'tidak ada paket yang cocok'

print(f'paket yang sesuai: {paket}')
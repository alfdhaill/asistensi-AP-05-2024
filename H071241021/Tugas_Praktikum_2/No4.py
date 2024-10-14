JumlahData = int(input('Masukkan jumlah data yang digunakan: '))
WaktuPenggunaan = input('Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak): '). lower ()
JenisPengguna = input('Apakah anda pengguna personal atau bisnis?: '). lower()

if JumlahData < 10 and WaktuPenggunaan == 'off-peak' and JenisPengguna == 'personal':
    Paket = 'Paket A'
elif 10 <= JumlahData <= 50 and WaktuPenggunaan == 'peak' and JenisPengguna == 'personal':
    Paket = 'Paket B'
elif JumlahData > 50 and WaktuPenggunaan == 'peak' and JenisPengguna == 'personal' and 'bisnis':
    Paket = 'Paket C'
elif JumlahData > 50 and WaktuPenggunaan == 'off-peak' and JenisPengguna == 'bisnis':
    Paket = 'Paket D'
else:
    Paket = 'tidak ada paket yang cocok'

print (f'paket yang sesuai: {Paket}')
    
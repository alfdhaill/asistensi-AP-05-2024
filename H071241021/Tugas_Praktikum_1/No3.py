print ('Konversi Jam ke Detik')

TotalDetik = int (input('Masukkan jumlah detik : '))

Jam = TotalDetik // 3600
Menit = (TotalDetik % 3600)//60
Detik = TotalDetik % 60

print(f'{Jam}:{Menit}:{Detik}')
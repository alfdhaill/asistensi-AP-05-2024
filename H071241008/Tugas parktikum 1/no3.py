print('konversi detik ke jam')
input = int(input('masukkan jumlah detik: '))
jam = input // 3600
modulusDetik = input % 3600
menit = (input % 3600) // 60
detik = modulusDetik % 60
print(f'{jam}:{menit:02}:{detik:02}')
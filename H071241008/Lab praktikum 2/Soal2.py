usia = int(input('masukkan usia: '))
anggota = input('apakah anda anggota (ya/tidak ?): ')

if usia < 5 :
    harga = 0
elif 5 <= usia <= 12 :
    harga = 50000
elif 13 <= usia <= 59 :
    harga = 100000
else:
    harga = 70000

harga_tiket = int(harga // 1.25 if anggota == 'ya' else harga)
                  
print(f'harga tiket: RP{harga_tiket}')
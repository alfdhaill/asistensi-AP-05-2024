sahamHariIni = 105.0
sahamKemarin = float(input('masukkan harga saham kemarin : '))

persentasePerubahan = ((sahamHariIni - sahamKemarin) / sahamKemarin) * 100

beli = (persentasePerubahan > 5)
jual = (persentasePerubahan < -3)
tahan = (persentasePerubahan >= -3) * (persentasePerubahan <= 5)


rekomendasi = beli * 'Beli' + jual * 'Jual' + tahan * 'Tahan'

print (f'perubahan persentase harga saham: {persentasePerubahan:.2f}%')
print (f'rekomendasi investasi: {rekomendasi}')
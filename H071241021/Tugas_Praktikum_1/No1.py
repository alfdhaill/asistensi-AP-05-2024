HargaSahamKemarin = float(input('Harga saham kemarin :'))
HargaSahamHariIni = 105

PerubahanPresentase = (( HargaSahamHariIni - HargaSahamKemarin) / HargaSahamKemarin) *100

Beli = PerubahanPresentase > 5
Jual = PerubahanPresentase < -3
Tahan = (PerubahanPresentase <= 5) * (PerubahanPresentase >= -3)

rekomendasi = Beli * 'Beli' + Tahan * 'Tahan' + Jual * 'Jual'


print (f'perubahan presentase harga saham {PerubahanPresentase:.2f}%')
print (f'rekomendasi presentase yang harus diambil adalah {rekomendasi}')
hargaKemarin = 105.0
hargaHariIni = float(input("Masukkan harga saham kemarin : "))

perubahanPersentase = ((hargaKemarin - hargaHariIni) / hargaKemarin) * 100

rekomendasi = 'Beli' * (perubahanPersentase > 5) + \
    'Tahan' * (perubahanPersentase <= 5 and perubahanPersentase >= -3) + \
    'Jual' * (perubahanPersentase < -3)

print(f'Perubahan persentase harga saham : {perubahanPersentase:.2f}%')
print(f"Rekomendasi investasi: {rekomendasi}")

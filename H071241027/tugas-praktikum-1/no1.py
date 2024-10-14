harga_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_hari_ini = 105.0 

perubahanPersentase = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100


rekomendasi = 'Beli' * (perubahanPersentase > 5) + \
    'Tahan' * (perubahanPersentase < 5 and perubahanPersentase > -3) + \
    'Jual' * (perubahanPersentase < -3)

print(f"Rekomendasi investasi: {rekomendasi}")
print(f"Perubahan persentasi harga saham {perubahanPersentase:.2f}%")
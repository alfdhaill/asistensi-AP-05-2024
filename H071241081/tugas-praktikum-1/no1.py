harga_saham_kemarin = float(input('harga saham kemarin : '))
harga_saham_hari_ini= 105

perubahan_presentasi = (( harga_saham_hari_ini - harga_saham_kemarin)/ harga_saham_kemarin) *100

beli = perubahan_presentasi >5
jual = perubahan_presentasi <-3
tahan = (perubahan_presentasi  <= 5 ) * (perubahan_presentasi >=-3 )

rekomendasi = beli* 'Beli' + jual * 'Jual'+ tahan * 'Tahan'


print (f'perubahan presentasi harga saham {perubahan_presentasi:.2f}%')
print (f'rekomdasi investasi {rekomendasi}')
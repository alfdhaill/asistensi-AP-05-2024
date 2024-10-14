usia = int(input('Masukkan Usia : '))
anggota = input('Apakah anda anggota (ya/tidak) :' ).lower() == 'ya'

if usia < 5:
    harga = 0
elif 5 <= usia <= 12:
    harga = 50000
elif 13 <= usia <= 59:
    harga = 100000
else:
    harga = 70000

print (f'Harga Tiket = Rp. {harga*0.8 if anggota else harga :.0f}')


    
       


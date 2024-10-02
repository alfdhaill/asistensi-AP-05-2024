PecahanUang = (100000, 50000, 20000, 10000, 5000, 2000, 1000)

TotalHarga = int(input('Masukkan Total Harga : '))
Uang = int(input('Masukkan Uang yang Diberikan : '))

if Uang < TotalHarga :
    print ('Uang Tidak Cukup')
else :
    Kembalian = Uang - TotalHarga
    print (f'Kembalian {Kembalian:,}')

    for Pecahan in PecahanUang:
        Lembaran = Kembalian // Pecahan
        Kembalian = Kembalian % Pecahan 
        if Lembaran > 0:
            print (f'{Lembaran} lembar Rp{Pecahan:,}')
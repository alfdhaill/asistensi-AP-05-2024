total_harga = int(input('Masukkan total harga: '))
uyd = int(input('Masukkan uang yang di berikan: '))
pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

kembalian = uyd - total_harga
print(f'sisa uang: {kembalian}')
print('bentuk dalam pecahan: ')

for i in pecahan:
    lembar = kembalian // i
    if lembar > 0 :
        print(f'{lembar} lembar uang {i}')
    kembalian %= i

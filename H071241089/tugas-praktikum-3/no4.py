try:
    harga = int(input('Masukkan total harga : '))
    inpUang = int(input('Masukkan uang yang diberikan : '))

    pecahanUang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

    kembalian = inpUang - harga

    if kembalian > 0:
        uangKembalian = {}

        for uang in pecahanUang:
            if kembalian >= uang:
                kembalian -= uang
                if uang in uangKembalian:
                    uangKembalian[uang] += 1
                else:
                    uangKembalian[uang] = 1

        for uang in uangKembalian:
            print(f"{uangKembalian[uang]} lembar Rp {uang:,}")
    elif kembalian == 0:
        print("Uang anda pas")
    else:
        print("Uang anda kurang")
except ValueError:
    print("Mohon input angka")

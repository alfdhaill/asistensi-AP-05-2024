total_harga = int(input("Masukkan Total Harga : "))
uang_diberi = int(input("Masukkan Uang Yang Diberikan : "))

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian = uang_diberi - total_harga


if kembalian == 0:
        print("Uang Yang Diberikan Pas")
        
elif uang_diberi < total_harga:
        print("Uang yang diberikan tidak cukup")
        
    
else :
    for uang in pecahan_uang:
        jumlah_lembar = kembalian // uang
        kembalian %= uang
        if jumlah_lembar > 0:
                print(jumlah_lembar, "lembar Rp." + format(uang, ","))
try:
    total_harga = int(input("Masukkan total harga yang harus dibayarkan: "))
    jumlah_uang = int(input("Masukkan jumlah uang yang diberikan oleh pelanggan: "))
        
    if jumlah_uang < total_harga:
        print("Uang yang diberikan tidak cukup.")
    elif total_harga < 0:
        print("Masukkan angka yang valid")
        
    kembalian = jumlah_uang - total_harga
    print(f"Kembalian = {kembalian:,} Rupiah")
    
    # Pecahan uang yang tersedia
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    rincian_kembalian = {}

    for uang in pecahan:
        jumlah_lembar = kembalian // uang
        if jumlah_lembar > 0:
            rincian_kembalian[uang] = jumlah_lembar
            kembalian -= uang * jumlah_lembar

    print("Rincian kembalian:")
    for uang, jumlah in rincian_kembalian.items():
        print(f"{jumlah} lembar uang {uang:,} Rupiah")
except:
    print("Masukkan angka yang valid.")

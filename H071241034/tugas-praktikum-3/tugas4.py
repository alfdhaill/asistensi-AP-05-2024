
# harga dan jumlah uang yang diberikan
total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan uang yang diberikan: "))
pecahan_uang= [100000, 50000,20000, 10000,5000,2000,1000]
 

# Hitung kembalian
kembalian = uang_diberikan - total_harga

# Cek  uang yang diberikan apakah  cukup
if kembalian < 0:
    print("Uang yang diberikan tidak cukup.")
else:
    print(f"Kembalian: Rp {kembalian:,}")  # Menampilkan kembalian dengan format ribuan
    
    # Looping untuk menghitung jumlah lembar per pecahan
    for pecahan in pecahan_uang:
        if kembalian >= pecahan:
            jumlah_lembar = kembalian //  pecahan
            print(f"{jumlah_lembar} lembar Rp {pecahan:,}")  # Menampilkan pecahan dengan koma
            kembalian %= pecahan  # Sisa kembalian 


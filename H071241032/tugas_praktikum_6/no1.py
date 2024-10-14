barang = []
def tambah():
    global barang
    kode = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
        harga_perunit = int(input("Masukkan harga per unit: "))
    except ValueError:
        print("Hanya angka yang berlaku")
        main()
    if jumlah < 1:
            print("jumlah barang tidak boleh kurang dari 0")
            main()
    if harga_perunit < 0:
        print("harga per unit barang tidak boleh kurang dari 0")
        main()
    barang.append({
        "kode": kode,
        "nama": nama,
        "jumlah": jumlah,
        "harga_perunit": harga_perunit
    })
    print("barang berhasil ditambahkan")
def tampilkan():
    global barang
    for i in range(len(barang)):
        print(f"Kode: {barang[i]['kode']}, Nama: {barang[i]['nama']}  Jumlah: {barang[i]['jumlah']} Harga per unit: {barang[i]['harga_perunit']}")
    if  len(barang) == 0:
        print("lagi kosong bos")
def  hapus():
    global barang
    x = print(f"Kode barang yang ada : {', '.join([i['kode'] for i in barang])}")
    kode = input(f"Masukkan kode barang yang ingin dihapus: ")
    for i in range(len(barang)):
        if kode == barang[i]['kode']:
            del barang[i]
            print("barang berhasil dihapus")
            break
        else:
            print("barang tidak ditemukan")
def cari():
    global barang
    mencari = input("Cari berdasarkan (1) Kode barang (2) Nama barang: ")
    if mencari in barang:
        
        if (mencari == "1"):
            kode = input("Masukkan kode barang yang ingin dicari: ")
            for i in range(len(barang)):
                if(barang[i]['kode'] == kode):
                    print(f"Kode: {barang[i]['kode']}, Nama: {barang[i]['nama']}, Jumlah: {barang[i]['jumlah']}, harga per unit: {barang[i]['harga_perunit']}")
                else:
                    print("barang tidak ditemukan")
        elif  (mencari == "2"):
            nama = input("Masukkan nama barang yang ingin dicari: ")
            for i in range(len(barang)):
                if(barang[i]['nama'] == nama):
                    print(f"Kode: {barang[i]['kode']}, Nama: {barang[i]['nama']}, Jumlah: {barang[i]['jumlah']}, harga per unit: {barang[i]['harga_perunit']}")
                else:
                    print("barang tidak ditemukan")
    else:
        print("Barang tidak ada")
def update():
    global barang
    x = print(f"Kode barang yang ada : {', '.join([i['kode'] for i in barang])}")
    kode = input("Masukkan kode barang yang ingin di update: ")
    if (kode  in [i['kode'] for i in barang]):
        try:
            n = int(input("Masukkan jumlah baru: "))
            if n < 1:
                print("jumlah barang tidak boleh kurang dari 0")
                main()
            h = int(input("Masukkan harga baru: "))
            if h < 0:
                print("jumlah barang tidak boleh kurang dari 0")
                main()
        except ValueError:
            print("Angka saja")
            main()
        for i in range(len(barang)):
            if(barang[i]['kode'] == kode):
                barang[i]['jumlah'] = n
                barang[i]['harga_perunit'] = h
                print("barang berhasil diupdate")
    else:
        print("Kode tidak ditemukan")
def main():
    global barang
    print("1. Tambah barang")
    print("2. Hapus barang")
    print("3. Tampilkan barang")
    print("4.  Cari barang")
    print("5. Update barang")
    print("6. Keluar")
    while True:
        pilihan = input("Pilih angka 1 - 6: ")
        if (pilihan == "1"):
            tambah()                   
            print("=================")
            print("1. Tambah barang")
            print("2. Hapus barang")
            print("3. Tampilkan barang")
            print("4.  Cari barang")
            print("5. Update barang")
            print("6. Keluar")
        elif (pilihan == "2"):
            hapus()
            print("=================")
            print("1. Tambah barang")
            print("2. Hapus barang")
            print("3. Tampilkan barang")
            print("4.  Cari barang")
            print("5. Update barang")
            print("6. Keluar")
        elif (pilihan == "3"):
            tampilkan()
            print("=================")
            print("1. Tambah barang")
            print("2. Hapus barang")
            print("3. Tampilkan barang")
            print("4.  Cari barang")
            print("5. Update barang")
            print("6. Keluar")
        elif (pilihan == "4"):
            cari()
            print("=================")
            print("1. Tambah barang")
            print("2. Hapus barang")
            print("3. Tampilkan barang")
            print("4.  Cari barang")
            print("5. Update barang")
            print("6. Keluar")
        elif (pilihan == "5"):
            update()
            print("=================")
            print("1. Tambah barang")
            print("2. Hapus barang")
            print("3. Tampilkan barang")
            print("4.  Cari barang")
            print("5. Update barang")
            print("6. Keluar")
        elif (pilihan == "6"):
            print("Makasih bang")
            return
        else:
            print("1. Tambah barang")
            print("2. Hapus barang")
            print("3. Tampilkan barang")
            print("4.  Cari barang")
            print("5. Update barang")
            print("6. Keluar")
main()
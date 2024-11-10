inventory = {}

def tambah_barang():
    kode = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
        if jumlah <= 0:
            raise ValueError("Jumlah harus bilangan bulat positif.")
    except ValueError as e:
        print(e)
        return

    try:
        harga = float(input("Masukkan harga barang: "))
        if harga <= 0:
            raise ValueError("Harga harus bilangan positif.")
    except ValueError as e:
        print(e)
        return
    
    inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
    print(f"Barang {nama} berhasil ditambahkan!")

def hapus_barang():
    kode = input("Masukkan kode barang yang ingin dihapus: ")
    if kode in inventory:
        del inventory[kode]
        print("Barang berhasil dihapus!")
    else:
        print("Barang tidak ditemukan!")

def tampilkan_barang():
    if inventory:
        for kode, data in inventory.items():
            print(f"Kode: {kode}, Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("Tidak ada barang di inventory.")

def cari_barang():
    kode = input("Masukkan kode barang yang dicari: ")
    if kode in inventory:
        data = inventory[kode]
        print(f"Barang ditemukan: Nama: {data['nama']}, Jumlah: {data['jumlah']}, Harga: {data['harga']}")
    else:
        print("Barang tidak ditemukan!")

def update_barang():
    tampilkan_barang()  
    kode = input("Masukkan kode barang yang ingin diupdate: ")

    if kode in inventory:
        nama = input("Masukkan nama barang baru: ")
        
        try:
            jumlah = int(input("Masukkan jumlah barang baru: "))
            if jumlah <= 0:
                raise ValueError("Jumlah harus bilangan bulat positif.")
        except ValueError as e:
            print(e)
            return

        try:
            harga = float(input("Masukkan harga barang baru: "))
            if harga <= 0:
                raise ValueError("Harga harus bilangan positif.")
        except ValueError as e:
            print(e)
            return

        inventory[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print("Data barang berhasil diperbarui!")
    else:
        print("Barang tidak ditemukan!")

def menu():
    while True:
        print("\n1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

menu()

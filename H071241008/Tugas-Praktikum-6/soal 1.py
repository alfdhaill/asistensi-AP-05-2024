gudang = {}  

def menu():
    print(">>> Menu Gudang Barang <<<")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ").strip()
    return pilihan

def tambah_barang():
    try:
        kode = input("Masukkan kode barang: ").strip()
        if kode in gudang:
            print("Adami yang pake i carimi kode lain.")
            return

        nama = input("Masukkan nama barang: ").strip()

        while True:
            jumlah = int(input("Masukkan jumlah barang: "))
            if jumlah < 0 :
                print('kenapa ko mau tambah tapi ko tulis negatif')
            else:
                break

        while True:            
            harga = float(input("Masukkan harga barang: "))
            if harga <= 0 :
                print('ini juga nda boleh negatif')
            else:
                break

        gudang[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print(f"Barang '{nama}' berhasil ditambahkan.")
    except ValueError:
        print("Input jumlah atau harga tidak valid. Harus berupa angka.")

def hapus_barang():
    for kode, data in gudang.items():
            print(f"Kode: {kode} | Nama: {data['nama']} | Jumlah: {data['jumlah']} | Harga: {data['harga']}")
    kode = input("Masukkan kode barang yang akan dihapus: ").strip()
    if kode in gudang:
        del gudang[kode]
        print("Barang berhasil dihapus.")
    else:
        print("Kode barang tidak ditemukan.")

def tampilkan_barang():
    if gudang:
        print("=== Daftar Barang ===")
        for kode, data in gudang.items():
            print(f"Kode: {kode} | Nama: {data['nama']} | Jumlah: {data['jumlah']} | Harga: {data['harga']}")
    else:
        print("Tidak ada barang dalam gudang.")

def cari_barang():
        kode = input("Masukkan kode barang yang dicari: ").strip()
        if kode in gudang:
            data = gudang[kode]
            print(f"Kode: {kode} | Nama: {data['nama']} | Jumlah: {data['jumlah']} | Harga: {data['harga']}")       
        else:
            print("Kode barang tidak ditemukan.")

def updateBarang():
    try:
        for kode, data in gudang.items():
            print(f"Kode: {kode} | Nama: {data['nama']} | Jumlah: {data['jumlah']} | Harga: {data['harga']}")

        kode = input('Masukkan Kode barang yang mau di update: ')

        if kode in gudang:
            kode = input('Masukkan kode barang yang baru: ')
            nama = input('Masukkan nama barang yang baru: ')

            while True:
                jumlah = int(input('Masukkan jumlah barang yang baru: '))
                if jumlah < 0 :
                    print('nda bisa negatif')
                else:
                    break

            while True:
                harga = float(input('Masukkan harga barang yang baru: '))
                if harga <= 0:
                    print('harga nda boleh negatif')
                else:
                    break
        else:
            print('kode barang tidak ditemukan')
            return updateBarang()
    except ValueError:
        print('Input jumlah atau harga tidak valid. Harus berupa angka')
    
    gudang[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
    print(f'barang sudah di perbaharui')


def main():
    while True:
        pilihan = menu()
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            updateBarang()
        elif pilihan == '6':
            print('Terimakasih satria sudah kerja ini susah payah')
            return
        else:
            print('inputan tidak valid')
        return main()
    
main()
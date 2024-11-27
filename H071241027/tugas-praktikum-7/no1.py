import os
from datetime import datetime

# Nama file untuk menyimpan data
FILM_FILE = "daftar_film.txt"
TIKET_FILE = "daftar_tiket.txt"

path = os.path
mkdir = os.mkdir
scandir = os.scandir

if not path.exists("tickets"):
    mkdir("tickets")

if not path.exists("films"):
    mkdir("films")

# ======== Fungsi Manajemen Film (Admin) ========
def tambah_film(judul, genre):
    with open(FILM_FILE, "a") as file:
        file.write(f"{judul},{genre}\n")
    print(f"Film '{judul}' berhasil ditambahkan!")
    
def hapus_film(judul):
    if not os.path.exists(FILM_FILE):
        print("Tidak ada daftar film yang bisa dihapus.")
        return
    with open(FILM_FILE, "r") as file:
        films = file.readlines()
    with open(FILM_FILE, "w") as file:
        for film in films:
            if not film.startswith(judul):
                file.write(film)
    print(f"Film '{judul}' berhasil dihapus!")

def tampilkan_daftar_film():
    daftarFilm = [entry.name for entry in scandir("films") if entry.is_file()]    
    for idx, temp in enumerate(daftarFilm, start=1):
        print(f"{idx}. {temp}")

# ======== Fungsi Pembelian Tiket (Pengunjung) ========
def beli_tiket(nomorFilm):
    tampilkan_daftar_film()
    
    daftarTiket = [entry.name for entry in scandir("tickets") if entry.is_file()]    

    film = daftarTiket[nomorFilm - 1]

    tanggal = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    id_tiket = generate_id_tiket()
    tiketPath = path.join("tickets", id_tiket)
    detail = detailTiket(id_tiket, film, tanggal)

    createTiket = open(tiketPath, "w")
    createTiket.write(detail)

    createTiket.close()
    return True

def detailTiket(id_tiket, judul_film, tanggal):
    tiket = f"""
+-------------------------------------+
|            TIKET BIOSKOP            |
+-------------------------------------+
| ID Tiket : {id_tiket:<20} |
| Film     : {judul_film:<20} |
| Tanggal  : {tanggal:<20} |
+-------------------------------------+
|     Terima kasih telah membeli      |
|             tiket Anda!             |
+-------------------------------------+
"""
    return tiket

# ======== Fungsi Manajemen Tiket (Admin) ========
def tampilkan_daftar_tiket():
    daftarTiket = [entry.name for entry in scandir("tickets") if entry.is_file()]
    print("Daftar Tiket:")
    for idx, temp in enumerate(daftarTiket, start=1):
        print(f"{idx}. {temp}")
    
def tampilkan_detail_tiket(nomorTiket):
    daftarTiket = [entry.name for entry in scandir("tickets") if entry.is_file()]
    if not daftarTiket:
        print("Belum ada tiket yang tersedia.")
        return
    try:
        idTiket = daftarTiket[nomorTiket - 1]
        tiket = open("tickets/" + idTiket, "r")

        for baris in tiket:
            print(baris.strip())
            return
    except:
        print("Nomor tiket tidak valid")
        return

def hapus_tiket(nomorTiket):
    daftarTiket = [entry.name for entry in scandir("tickets") if entry.is_file()]
    tampilkan_daftar_film()
    if not daftarTiket:
        print("Belum ada tiket yang tersedia.")
        return
    try:
        idTiket = daftarTiket[nomorTiket - 1]
        deleteTiket = open("tickets/" + idTiket, "x")
    except:
        return
    
# ======== Fungsi Tambahan ========
def generate_id_tiket():
    waktu_sekarang = datetime.now().strftime("%d%m%Y%H%M%S")
    return f"TICK{waktu_sekarang}"

def input_integer(prompt):
    """Menangani input berupa angka."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Input tidak valid. Masukkan angka!")

# ======== Menu Utama ========
def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Tampilkan Daftar Film")
        print("4. Tampilkan Daftar Tiket")
        print("5. Tampilkan Detail Tiket")
        print("6. Hapus Tiket")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Masukkan judul film: ")
            genre = input("Masukkan genre film: ")
            tambah_film(judul, genre)

        elif pilihan == "2":
            judul = input("Masukkan judul film yang ingin dihapus: ")
            hapus_film(judul)

        elif pilihan == "3":
            tampilkan_daftar_film()

        elif pilihan == "4":
            tampilkan_daftar_tiket()

        elif pilihan == "5":
            print("Daftar ID Tiket yang Tersedia:")
            with open(TIKET_FILE, "r") as file:
                tickets = file.readlines()
            for ticket in tickets:
                split_ticket = ticket.strip().split(",")
                print(f"ID Tiket: {split_ticket[0]}")
            id_tiket = input("Masukkan ID tiket: ")
            tampilkan_detail_tiket(id_tiket)

        elif pilihan == "6":
            print("Daftar ID Tiket yang Tersedia:")
            with open(TIKET_FILE, "r") as file:
                tickets = file.readlines()
            for ticket in tickets:
                split_ticket = ticket.strip().split(",")
                print(f"ID Tiket: {split_ticket[0]}")
            id_tiket = input("Masukkan ID tiket yang ingin dihapus: ")
            hapus_tiket(id_tiket)

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

def menu_pengunjung():
    while True:
        print("\n=== Menu Pengunjung ===")
        print("1. Tampilkan Daftar Film")
        print("2. Beli Tiket")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_daftar_film()

        elif pilihan == "2":
            tampilkan_daftar_film()
            
            while True:
                nomorFilm = input("Masukkan nomor film : ")
                
        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")


def main():
    while True:
        print("\n=== Sistem Informasi Bioskop ===")
        print("1. Admin")
        print("2. Pengunjung")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_admin()
        elif pilihan == "2":
            menu_pengunjung()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

main()
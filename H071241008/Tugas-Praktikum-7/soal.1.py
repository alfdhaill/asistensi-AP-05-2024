from datetime import datetime
import os

def tambah_film():
    film = input("Masukkan judul film (tekan Enter untuk batal): ")
    if film.strip() == "":
        print("Penambahan film dibatalkan.")
        return
    with open("films.txt", "a") as f:
        f.write(f"{film}\n")
    print(f"Film '{film}' berhasil ditambahkan!")
    
def tampilkan_film():
    if not os.path.exists("films.txt"):
        print("Tidak ada film yang tersedia.")
        return

    with open("films.txt", "r") as f:
        films = f.readlines()
    if films:
        print("Daftar Film:")
        for index, film in enumerate(films):
            print(f"{index + 1}. {film.strip()}")
    else:
        print("Tidak ada film yang tersedia.")

def hapus_film():
    if not os.path.exists("films.txt"):
        print("Belum ada film.")
        return

    while True:
        tampilkan_film()
        try:
            choice = int(input("Pilih film yang akan dihapus (atau ketik 0 untuk batal): "))
            if choice == 0:
                print("Penghapusan film dibatalkan.")
                break
            with open("films.txt", "r") as f:
                films = f.readlines()
            if 1 <= choice <= len(films):
                film_to_delete = films.pop(choice - 1)
                with open("films.txt", "w") as f:
                    f.writelines(films)
                print(f"Film '{film_to_delete.strip()}' berhasil dihapus.")
                break
            else:
                print(f"Pilih nomor antara 1 dan {len(films)}.")
        except ValueError:
            print("Masukkan angka yang valid.")

def update_film():
    tampilkan_film()
    try:
        choice = int(input("Pilih nomor film yang akan diperbarui (ketik 0 untuk batal): "))
        if choice == 0:
            print("Pembaruan film dibatalkan.")
            return

        with open("films.txt", "r") as f:
            films = f.readlines()
        
        if 1 <= choice <= len(films):
            new_title = input("Masukkan judul baru: ")
            films[choice - 1] = new_title + '\n'
            
            with open("films.txt", "w") as f:
                f.writelines(films)
            print(f"Judul film berhasil diperbarui menjadi '{new_title}'.")
        else:
            print(f"Pilih nomor antara 1 dan {len(films)}.")
    except ValueError:
        print("Masukkan angka yang valid.")


def beli_tiket():
    if not os.path.exists("films.txt"):
        print("Tidak ada film yang tersedia.")
        return

    while True:
        tampilkan_film()
        try:
            choice = int(input("Pilih nomor urutan film yang ingin ditonton (atau ketik 0 untuk batal): "))
            if choice == 0:
                print("Pembelian tiket dibatalkan.")
                return
            with open("films.txt", "r") as f:
                films = [line.strip() for line in f.readlines()]
            if 1 <= choice <= len(films):
                film = films[choice - 1]
                break
            else:
                print("Film yang Anda pilih tidak tersedia. Silakan pilih film yang ada.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    id_tiket = f"TICK{datetime.now().strftime('%d%m%Y%H%M%S')}"
    waktu = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    buat_file_tiket(id_tiket, film, waktu)
    print(f"Tiket berhasil dibeli! ID Tiket Anda: {id_tiket}")

def buat_file_tiket(id_tiket, film, waktu):
    folder = "tiket"
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, f"{id_tiket}.txt")
    with open(filepath, "w") as f:
        f.write("---------------------------------\n")
        f.write("|          TIKET BIOSKOP        |\n")
        f.write("---------------------------------\n")
        f.write(f"|ID Tiket : {id_tiket}\n")
        f.write(f"|Film     : {film}\n")      
        f.write(f"|Tanggal  : {waktu}\n")
        f.write("---------------------------------\n")
        f.write("Terima kasih telah menonton ditempat kami\n")
    print(f"Detail tiket tersimpan di '{filepath}'")

    if not os.path.exists("tickets.txt"):
        open("tickets.txt", "w").close()

    with open("tickets.txt", "a") as f:
        f.write(f"{id_tiket}, {film}, {waktu}\n")

def tampilkan_tiket():
    if not os.path.exists("tickets.txt"):
        print("Belum ada tiket yang dibeli.")
        return

    with open("tickets.txt", "r") as f:
        tickets = f.readlines()
    if tickets:
        print("Daftar Tiket:")
        for i, ticket in enumerate(tickets):
            print(f"{i + 1}. {ticket.strip()}")
    else:
        print("Belum ada tiket yang dibeli.")

def detail_tiket():
    while True:
        tampilkan_tiket()
        if not os.path.exists("tickets.txt"):
            return
        pilihan = input("Pilih nomor tiket untuk melihat detail (ketik 0 untuk batal): ")
        if pilihan == "0":
                return
        with open("tickets.txt", "r") as f:
            tickets = f.readlines()
        try:
            tiket_terpilih = tickets[int(pilihan) - 1].split(", ")
            id_tiket = tiket_terpilih[0]
            file_tiket = f"tiket/{id_tiket}.txt"
            if os.path.exists(file_tiket):
                with open(file_tiket, "r") as f:
                    print(f.read())
            else:
                print(f"Detail untuk tiket dengan ID {id_tiket} tidak ditemukan.")
        except (IndexError, ValueError):
            print("Pilihan tidak valid!")

def hapus_tiket():
    if not os.path.exists("tickets.txt"):
        print("Belum ada tiket yang dibeli.")
        return

    tampilkan_tiket()
    id_tiket = input("Masukkan ID tiket yang akan dihapus: ")
    with open("tickets.txt", "r") as f:
        tickets = f.readlines()
    with open("tickets.txt", "w") as f:
        for ticket in tickets:
            if id_tiket not in ticket:
                f.write(ticket)
    file_tiket = f"tiket/{id_tiket}.txt"
    if os.path.exists(file_tiket):
        os.remove(file_tiket)
        print(f"Tiket dengan ID {id_tiket} berhasil dihapus.")
    else:
        print(f"Tiket dengan ID {id_tiket} tidak ditemukan.")

def login_admin():
    while True:
        print("\nMenu:")
        print("1. Tambah Film")
        print("2. Tampilkan Film")
        print("3. Hapus Film")
        print("4. Update Film")
        print("5. Tampilkan Tiket")
        print("6. Detail Tiket")
        print("7. Hapus Tiket")
        print("0. Keluar")

        pilihan = input("Pilih opsi: ")
        
        if pilihan == "1":
            tambah_film()
        elif pilihan == "2":
            tampilkan_film()
        elif pilihan == "3":
            hapus_film()
        elif pilihan == "4":
            update_film()
        elif pilihan == "5":
            tampilkan_tiket()
        elif pilihan == "6":
            detail_tiket()
        elif pilihan == "7":
            hapus_tiket()
        elif pilihan == "0":
            ("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def menu_pengunjung():
    while True:
        print("\nMenu Pengunjung:")
        print("1. Tampilkan Daftar Film")
        print("2. Beli Tiket")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_film()
        elif pilihan == "2":
            beli_tiket()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")

while True:
    print("\nSistem Informasi Bioskop")
    print("1. Masuk sebagai Admin")
    print("2. Masuk sebagai Pengunjung")
    print("3. Keluar")
    pilihan = input("Pilih peran: ")

    if pilihan == "1":
        login_admin()
    elif pilihan == "2":
        menu_pengunjung()
    elif pilihan == "3":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid!")
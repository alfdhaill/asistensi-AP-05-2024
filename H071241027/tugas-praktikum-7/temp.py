from datetime import datetime
from os import mkdir, path, scandir, remove

if not path.exists("films"):
    mkdir("films")

if not path.exists("tickets"):
    mkdir("tickets")

def handleInput(inputMsg, tipe):
    while True:
        try:
            inputField = tipe(input(inputMsg))
            return inputField
        except ValueError:
            print("Input tidak sesuai tipe, coba lagi.")

def tampilkanDaftar(judul: str, daftar: list, format=1, kosong = False):
    if format == 1:
        print(f"--- {judul} ---")
    else:
        print(f"{judul}:")
    
    if kosong:
        kataKedua = judul.split(" ")[1]
        print(f"{kataKedua} Kosong")
    else:
        for idx, val in enumerate(daftar, start=1):
            print(f"{idx}. {val}")

def generateId():
    waktu = datetime.now()
    id = waktu.strftime("%d%m%Y%H%M%S")
    return "TICK" + id

def getTanggalNow():
    tanggal = datetime.now()
    formattedTanggal = tanggal.strftime("%d-%m-%Y %H:%M:%S")
    return formattedTanggal

def generateDetailTiket(namaFilm: str, id: str, tanggal: str):
    baris = []

    stringFilm = 13 + len(namaFilm) + 2  
    stringId = 18 + len(id) + 2           
    stringTanggal = 19 + 13 + 2 

    stringTerpanjang = max(stringFilm, stringId, stringTanggal)

    baris.append(f"+{'-' * stringTerpanjang}+\n")
    
    teksTiket = "Tiket Bioskop"
    paddingKiri = (stringTerpanjang - len(teksTiket)) // 2
    paddingKanan = stringTerpanjang - len(teksTiket) - paddingKiri
    baris.append(f"|{' ' * paddingKiri}{teksTiket}{' ' * paddingKanan}|\n")

    baris.append(f"+{'-' * stringTerpanjang}+\n")

    baris.append(f"| ID Tiket : {id}{' ' * (stringTerpanjang - len(id) - 12)}|\n")
    baris.append(f"| Film     : {namaFilm}{' ' * (stringTerpanjang - len(namaFilm) - 12)}|\n")
    baris.append(f"| Tanggal  : {tanggal}{' ' * (stringTerpanjang - len(tanggal) - 12)}|\n")
    baris.append(f"+{'-' * stringTerpanjang}+\n")

    return baris

def tambahFilm():
    while True:
        print()
        print("--- Tambah Film ---")       
        namaFilm = handleInput("Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ", str) 
        pathFilm = path.join("films", namaFilm)

        if namaFilm == "":
            return
        elif path.exists(pathFilm):
            print("Film sudah ada")
        else:
            print()
            print(f"Film '{namaFilm}' berhasil ditambahkan")
            print()

            createFilm = open(pathFilm, "w")
            createFilm.close()

def hapusFilm():
    while True:
        print()    
        listFilm = [entry.name for entry in scandir("films") if entry.is_file()]
        tampilkanDaftar("Daftar Film", listFilm, kosong=len(listFilm) == 0)
        if not len(listFilm) == 0:
            print("0. Kembali")
            film = handleInput("Pilih nomor film yang ingin dihapus (atau 0 untuk kembali): ", int)
            if film == 0:
                return
            try:
                filmDipilih = listFilm[film - 1]
                pathFilm = path.join("films", filmDipilih)
                remove(pathFilm)
                print(f"Film '{filmDipilih}' berhasil dihapus")
            except:
                print("Film tidak valid")
                return
        else:
            return

def lihatDaftarTiket(listTiket):
    print()
    print("Daftar Tiket:")
    for idx, tiket in enumerate(listTiket, start=1):
        print(f"{idx}. {tiket[:-4]}")

def hapusTiket(listTiket):
    while True:
        print()
        print("--- Detail Tiket ---")
        print("Daftar Tiket:")
        for idx, tiket in enumerate(listTiket, start=1):
            print(f"{idx}. {tiket[:-4]}")
        print("0. Kembali")
        print()

        tiket = handleInput("Pilih nomor tiket yang ingin dihapus (atau 0 untuk kembali): ", int)

        if tiket > len(listTiket):
            print("Tiket tidak valid")
            tiket = handleInput("Pilih nomor tiket yang ingin dihapus (atau 0 untuk kembali):", int)
        
        if tiket == 0:
            return
        
        tiketDipilih = listTiket[tiket - 1]
        tiketPath = path.join("tickets", tiketDipilih)

        remove(tiketPath)

        print("Berhasil menghapus tiket")

        return

def detailTiket(listTiket):
    while True:
        print()
        print("--- Detail Tiket ---")
        lihatDaftarTiket(listTiket)
        print("0. Kembali")
        print()

        tiket = handleInput("Pilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): ", int)

        if tiket > len(listTiket):
            print("Tiket tidak valid")
            tiket = handleInput("Pilih nomor tiket yang ingin dilihat (atau 0 untuk kembali):", int)
        
        if tiket == 0:
            return
        
        tiketDipilih = listTiket[tiket - 1]
        tiketPath = path.join("tickets", tiketDipilih)

        with open(tiketPath, "r") as file:
            for line in file:
                print(line.strip())

def daftarTiket():
    while True:
        print()
        menu = ["Lihat Daftar Tiket", "Lihat Detail Tiket", "Hapus Tiket", "Kembali"]
        listTiket = [entry.name for entry in scandir("tickets") if entry.is_file()]
        tampilkanDaftar("Daftar Tiket", menu, kosong=len(listTiket) == 0)

        if listTiket:
            opsi = handleInput("Pilih opsi (1/2/3/4): ", int)

            match opsi:
                case 1:
                    lihatDaftarTiket(listTiket)
                case 2:
                    detailTiket(listTiket)
                case 3:
                    hapusTiket(listTiket)
                case 4:
                    return
        else:
            return

def beliTiket(listFilm):
    while True:
        print()
        listFilm = [entry.name for entry in scandir("films") if entry.is_file()]
        belumAdaFilm = len(listFilm) == 0
        tampilkanDaftar("Daftar Film", listFilm, kosong=belumAdaFilm)

        if not belumAdaFilm:
            print("0. Kembali")
            film = handleInput("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): ", int)

            if film not in range(len(listFilm) + 1):
                print('Film tidak valid')
            elif film == 0:
                return
            else:
                filmDipilih = listFilm[film - 1]
                id = generateId()
                tanggal = getTanggalNow()
                baris = generateDetailTiket(filmDipilih, id, tanggal)
                fileTiket = id + ".txt"
                tiketPath = path.join("tickets", fileTiket)

                try:
                    with open(tiketPath, "w") as createTiket:
                        createTiket.writelines(baris)

                    print()
                    print(f"Tiket berhasil dibeli. ID tiket Anda: {id}")
                    print(f"File tiket telah dibuat di tickets/{fileTiket}")
                    print()
                except Exception as e:
                    print(e)
                    return
        else:
            print()
            return

def menuAdmin():
    while True:
        print()
        menu = ["Tambah Film", "Hapus Film", "Daftar Tiket", "Kembali"]
        tampilkanDaftar("Menu Admin", menu)
        opsi = handleInput("Pilih opsi (1/2/3/4): ", int)

        if opsi not in range(1, 5):
            print("Opsi tidak valid")
            opsi = handleInput("Pilih opsi (1/2/3/4): ", int)
        
        match opsi:
            case 1:
                tambahFilm()
            case 2:
                hapusFilm()
            case 3:
                daftarTiket()
            case 4:
                return

def menuPengunjung():
    while True:
        menu = ["Lihat daftar film", "Beli Tiket", "Kembali"]
        tampilkanDaftar("Menu Pengunjung", menu)
        opsi = handleInput("Pilih opsi (1/2/3): ", int)
        listFilm = [entry.name for entry in scandir("films") if entry.is_file()]

        if opsi not in range(1, 4):
            print("Opsi tidak valid")
            opsi = handleInput("Pilih opsi (1/2/3): ", int)
        match opsi:
            case 1:
                print()
                tampilkanDaftar("Daftar Film", listFilm, kosong=len(listFilm) == 0)
                print()
            case 2:
                beliTiket(listFilm)
            case 3:
                return

while True:
    menu = ["Admin", "Pengunjung", "Keluar"]
    tampilkanDaftar("Sistem Pemesanan Tiket Bioskop", menu)
    peran = handleInput("Pilih peran (1/2/3): ", int)

    if peran == 3:
        print("Terima kasih telah menggunakan aplikasi ini")
        break
    elif peran not in range(1, 4):
        print("Peran tidak sesuai")
        peran = handleInput("Pilih peran (1/2/3): ", int)
    
    print()

    if peran == 1:
        menuAdmin()
    else:
        menuPengunjung()

    print()
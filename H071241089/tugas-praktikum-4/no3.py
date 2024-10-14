def prosesAngka(n: int):
    if n <= 0:
        raise Exception("Input bilangan bulat positif")
    elif n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1


try:
    angka = int(input("Masukkan angka: "))
    jumlahLangkah = 0

    while angka != 1:
        jumlahLangkah += 1
        angka = prosesAngka(angka)
        print(angka)

    print("Jumlah langkah:", jumlahLangkah)
except Exception as e:
    print(e)
except ValueError:
    print("Input tidak Valid")

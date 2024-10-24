def sandi_caesar(teks, pergeseran):
    alfabet_kecil = 'abcdefghijklmnopqrstuvwxyz'
    alfabet_besar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    hasil_enkripsi = ""
    for karakter in teks:
        if karakter in alfabet_kecil:
            indeks_baru = (alfabet_kecil.find(karakter) + pergeseran) % 26
            hasil_enkripsi += alfabet_kecil[indeks_baru]
        elif karakter in alfabet_besar:
            indeks_baru = (alfabet_besar.find(karakter) + pergeseran) % 26
            hasil_enkripsi += alfabet_besar[indeks_baru]
        else:
            hasil_enkripsi += karakter
    return hasil_enkripsi
teks = input("Masukkan Teks: ")
pergeseran = int(input("Masukkan jumlah pergeseran: "))
text = print(f"Tekst : {teks}")
shift = print(f"Shift : {pergeseran}")

teks_terenkripsi = sandi_caesar(teks, pergeseran)
print(f"Hasil Enkripsi: {teks_terenkripsi}")


karakter = input("Masukkan sebuah abjad : ")
kalimat = input("Masukkan Kalimat : ")

pesan = f"{karakter} merupakan bagian dari '{kalimat}'" * (karakter in kalimat) + \
        f"{karakter} tidak ditemukan dalam '{kalimat}'" * (karakter not in kalimat)

print(pesan)
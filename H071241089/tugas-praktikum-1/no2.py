abjad = input("Masukkan sebuah abjad : ")
kalimat = input("Masukkan Kalimat : ")

pesan = f'{abjad} merupakan bagian dari "{kalimat}"' * (abjad in kalimat) + \
        f'{abjad} tidak ditemukan dalam "{kalimat}"' * \
    (abjad not in kalimat)

print(pesan)

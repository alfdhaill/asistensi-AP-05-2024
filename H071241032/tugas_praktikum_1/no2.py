karakter = input('masukkan karakter : ')
kalimat = input('masukkan kalimat : ')

result = f"{karakter} Ditemukan dalam {kalimat}" * (karakter in kalimat) + \
         f"{karakter} Tidak ditemukan dalam {kalimat}"* (karakter not in kalimat)
print(result)

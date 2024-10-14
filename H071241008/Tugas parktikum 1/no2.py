karakter = input('masukkan karakter: ')
kalimat = input('masukkan kalimat: ')

print(f'{karakter} ditemukan dalam "{kalimat}"'*(karakter in kalimat) + 
      f'{karakter} tidak ditemukan dalam "{kalimat}"'*(karakter not in kalimat))

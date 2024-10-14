karakter = input("masukan karakter : ")
kalimat = input('masukan kalimat : ')

print (f'"{karakter}" tidak ditemukan dalam "{kalimat}"'* (karakter not in kalimat )+ f' {karakter} ditemukan dalam "{kalimat}"'* (karakter in kalimat))

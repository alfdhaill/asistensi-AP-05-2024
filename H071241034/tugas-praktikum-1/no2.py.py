# Input karakter dan kalimat dari pengguna
karakter = input("Masukkan karakter: ")
kalimat = input("Masukkan kalimat: ")

# Periksa apakah karakter ada di dalam kalimat dan tampilkan pesan sesuai
print (f"{karakter} ditemukan dalam '{kalimat}'" * (karakter in kalimat) + 
      f"{karakter} tidak ditemukan dalam '{kalimat}' " * (karakter not in kalimat))

print("## Program Karakter dalam Kalimat ##")
print("===========================")
print()

karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan Kalimat : ")

cek_karakter = (karakter in kalimat) and f"{karakter} terdapat dalam \"{kalimat}\"" or f"{karakter} tidak terdapat dalam \"{kalimat}\""

print(cek_karakter)
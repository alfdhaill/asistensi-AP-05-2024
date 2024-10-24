def acronim(n):
    acronim = ""
    i = n.split()
    for m in i:
        acronim += m[0].upper()
    return acronim
kalimat = input("Masukkan Kalimat: ")
print(acronim(kalimat)) 
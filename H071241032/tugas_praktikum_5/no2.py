import os
os.system("cls")
def acronim(kalimat):
    a = kalimat.upper()
    b = a.split()
    for i in b:
        i = i[0]
        print(i, end="")
acronim("agdua f uad")
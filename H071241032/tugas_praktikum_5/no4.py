import os
os.system("cls")
def turunan(kalimat):
    for i in range(1, len(kalimat)+ 1):
        for j in range(len(kalimat)- i + 1):
            print(kalimat[j:j+i])
n = input("masukkan kata: ")
turunan(n)
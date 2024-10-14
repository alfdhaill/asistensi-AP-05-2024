import os
os.system("cls")
def palindrome(kalimat):
    kata = kalimat.lower()
    balik = kata.replace(" ","")
    if kata == balik[::1]:
        print("on")
    else:
        print("off")
palindrome("apa")
    
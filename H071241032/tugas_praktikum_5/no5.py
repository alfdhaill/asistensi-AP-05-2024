import os
os.system("cls")
alphabet = "abcdefghijklmnopqrstuvwxyz"
string = input("Masukkan kata: ")
geser= int(input("Masukkan shift: ")) 
kata = string.lower()
hasil = ""                                     
for i in kata:
    if i in alphabet:
        index = alphabet.index(i)
        pergeseran = (index + geser) % 26 
        hasil += alphabet[pergeseran]
    else:
        hasil += i
print("Text:",string)
print("Shift:",geser)
print("Cipher:",hasil)
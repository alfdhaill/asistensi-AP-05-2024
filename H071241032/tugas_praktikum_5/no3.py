import os
os.system("cls")
def anagram(s1,s2):
    pengahapusan = {}
    for karakter in s1:
        pengahapusan[karakter]=pengahapusan.get(karakter,0)+1
    for karakter in s2:
        pengahapusan[karakter]=pengahapusan.get(karakter,0)-1
    total_hapus = sum(abs(count)for count in pengahapusan.values())
    return total_hapus
s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ")
hasil = anagram(s1,s2)
print(f"jumlah minimum penghapusan adalah: {hasil}")
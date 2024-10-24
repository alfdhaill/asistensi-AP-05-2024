def menghapus_anagram(s1, s2):
    # Ubah string menjadi list agar bisa dimodifikasi
    list_s1 = list(s1)
    list_s2 = list(s2)
    
    # Iterasi setiap karakter di string pertama
    for karakter in s1:
        if karakter in list_s2:
            # Jika karakter ada di string kedua, hapus dari kedua string
            list_s1.remove(karakter)
            list_s2.remove(karakter)
    
    # Jumlah penghapusan adalah total karakter yang tersisa di kedua list
    penghapusan = len(list_s1) + len(list_s2)
    
    return penghapusan

string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")

jumlah_penghapusan = menghapus_anagram(string1, string2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {jumlah_penghapusan}")


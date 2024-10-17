def hitung_hapus_anagram_v3(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)
    
    hapus_karakter = 0
    for char in set_s1.union(set_s2):
        hapus_karakter += abs(s1.count(char) - s2.count(char))
    return hapus_karakter

string1 = input('Masukkan string pertama: ')
string2 = input('Masukkan string kedua: ')

print(f"Jumlah penghapusan karakter: {hitung_hapus_anagram_v3(string1, string2)}")

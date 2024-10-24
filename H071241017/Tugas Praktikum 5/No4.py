def buat_substrings(s):
    substring = []
    panjang = len(s)

    for m in range(1, panjang + 1):
        for i in range(panjang - m + 1):
            substring.append(s[i:i + m])
    return substring

kalimat = input("Masukkan Kalimat: ")
substrings = buat_substrings(kalimat)
for substring in substrings:
    print(substring)
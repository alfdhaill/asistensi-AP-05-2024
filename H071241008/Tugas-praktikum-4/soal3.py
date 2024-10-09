def hitung_langkah(s):
    if not isinstance(s, int) or s <= 0:
        return "Input tidak Valid"
    langkah = 0
    print(f"Langkah ke-{langkah}: {s}")
    
    while s != 1:
        if s % 2 == 0:
            s //= 2
        else:
            s = s * 3 + 1
        langkah += 1
        print(f"Langkah ke-{langkah}: {s}")
    
    return (f"Total langkah: {langkah}")

try:
    s = int(input("Masukkan bilangan bulat positif: "))
    print(hitung_langkah(s))
except ValueError:
    print("Input tidak Valid")
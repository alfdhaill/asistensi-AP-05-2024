def caesar_cipher(text, shift):
    kecil = 'abcdefghijklmnopqrstuvwxyz'
    besar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ' '
    
    for char in text:
        if char in kecil:
            new_char = kecil[(kecil.index(char) + shift) % 26]
            result += new_char
        elif char in besar:
            new_char = besar[(besar.index(char) + shift) % 26]
            result += new_char
        else:
            result += char  
    return result

text = input("Masukkan string: ")
shift = int(input("Berapa kali ko mo geser: "))
print("geser geser:", caesar_cipher(text, shift))
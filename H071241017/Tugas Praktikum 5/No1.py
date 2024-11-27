def palindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
kalimat = input("Masukkan kata atau kalimat: ")
print(palindrome(kalimat)) 
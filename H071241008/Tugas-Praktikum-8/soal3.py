import re


def validate_username(username):
    pattern = r'^[a-zA-Z0-9]{5,20}$'
    return re.match(pattern, username)

def validate_email(email):
    pattern = r'^[a-z]+[a-z0-9]*@[a-z]+\.[a-z]{2,}(?:\.[a-z]{2,})?$'
    return re.match(pattern, email)

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(pattern, password)

def sambutan():
    username = validate_username()
    return username

def main():
    while True:
        username = input("Masukkan username: ")
        if validate_username(username):
            break
        print("Username tidak valid. (Panjang 5-20 karakter, hanya huruf dan angka). Registrasi gagal.")
        continue

    while True:
        email = input("Masukkan email: ")
        if validate_email(email):
            break
        print("Email tidak valid. (Format: username@example.com dan hanya huruf kecil). Registrasi gagal.")
        continue

    while True:
        password = input("Masukkan password: ")
        if validate_password(password):
            break
        print("Password tidak valid. (Minimal 8 karakter, mengandung huruf kapital, huruf kecil, dan angka, tanpa simbol).\nRegistrasi gagal.")
        continue
    print(f"Registrasi berhasil \nSelamat Datang {username}")

main()
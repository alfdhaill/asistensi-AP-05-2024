print("selamat datang di kalkulator sederhana")
def kalkulator():
    try:
        angka_pertama = float(input("Angka pertama = "))
    except ValueError :
        print("Input tidak valid, masukan angka")
    try:
        angka_kedua = float(input("Angka kedua = "))
    except ValueError :
        print("Input tidak valid, masukan angka")
    operasi = input("Operasi (+, -, *, :) = ")   
    try:
        if operasi == "*":
            print(f"hasil dari {angka_pertama} {operasi} {angka_kedua} adalah {angka_pertama*angka_kedua}")
        elif operasi == ":" :
            print(f"hasil dari {angka_pertama} {operasi} {angka_kedua} adalah {angka_pertama/angka_kedua}")
        elif operasi == "+" :
            print(f"hasil dari {angka_pertama} {operasi} {angka_kedua} adalah {angka_pertama+angka_kedua}")
        elif operasi == "-" :
            print(f"hasil dari {angka_pertama} {operasi} {angka_kedua} adalah {angka_pertama-angka_kedua}")
        else :
            print("operasi tak terdefinisi")
    except ValueError as e :
        print(f"operasi salah: {e}") 
kalkulator()

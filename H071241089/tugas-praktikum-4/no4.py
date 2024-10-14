print("Selamat datang di kalkulator Sederhana!")


def fungsiKalkulator(a, b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            raise Exception("Operasi tidak valid. Gunakan +, -, *, atau /.")


try:
    angkaPertama = float(input("Angka pertama: "))
    angkaKedua = float(input("Angka kedua: "))
    operator = input("Operasi (+, -, *, /): ")

    hasil = fungsiKalkulator(angkaPertama, angkaKedua, operator)

    print(hasil)
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Pembagian dengan nol tidak diperbolehkan.")
except Exception as e:
    print(e)

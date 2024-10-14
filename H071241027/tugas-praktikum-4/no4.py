def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    
    try:
        angka1 = float(input("Angka pertama: "))
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return
    
    try:
        angka2 = float(input("Angka kedua: "))
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return
    
    operasi = input("Operasi (+, -, *, /): ")
    
    if operasi not in ['+', '-', '*', '/']:
        print("Operasi tidak valid. Gunakan +, -, *, atau /")
        return
    
    if operasi == '+':
        hasil = angka1 + angka2
    elif operasi == '-':
        hasil = angka1 - angka2
    elif operasi == '*':
        hasil = angka1 * angka2
    elif operasi == '/':
        if angka2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
            return
        hasil = angka1 / angka2
    
    print(f"Hasil: {hasil}")

kalkulator()

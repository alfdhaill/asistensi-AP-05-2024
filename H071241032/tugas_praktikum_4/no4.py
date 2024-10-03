def kalkulator():
    print("SELAMAT DATANG DI KALKULATOR ANJAY")
    
    try:
        angka_pertama = float(input("Angka pertama: "))
    except ValueError as e:
        print(f"Input tidak valid: could not convert string to float: {e}")
        return

    try:
        angka_kedua = float(input("Angka kedua: "))
    except ValueError as e:
        print(f"Input tidak valid: could not convert string to float: {e}")
        return
    operasi = input("Operasi (+, -, *, /): ")

    if operasi == '+':
        hasil = angka_pertama + angka_kedua
        print(f"hasil: {hasil}")
    elif operasi == '-':
        hasil = angka_pertama - angka_kedua
        print(f"hasil: {hasil}")
    elif operasi == '*':
        hasil = angka_pertama * angka_kedua
        print(f"hasil: {hasil}")
    elif operasi == '/':
       if angka_kedua != 0:
           hasil = angka_pertama / angka_kedua
           print(f"hasil: {hasil}")
       else:
           print("pembagi tidak boleh 0 kocak, kagak bisa terdefinisi")
    else:
        if operasi != "+, -, *, /":
            print("Operasi tidak valid. Gunakan +, -, *, atau /")
    
kalkulator()

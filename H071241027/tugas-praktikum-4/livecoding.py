def kalkulator(aksi, angka1, angka2):
    if aksi =="+":
        return(angka1 + angka2)
    elif aksi =="-":
        return(angka1 - angka2)
    elif aksi =="*":
        return(angka1 * angka2)
    
    elif aksi =="/":
        if angka2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan")
        else :
            return(angka1 // angka2)

angka1 = float(input("Angka Pertama : "))
angka2 = float(input("Angka Kedua : "))
aksi = input("Operasi (+, -, *, /) :")

if aksi not in "+,-,*,/":
    print("Operasi tidak valid. Gunakan +,-,*,/")

print(kalkulator(aksi, angka1, angka2))
            
           
            
            

            
    












A = int(input("Masukkan populasi awal serangga A: "))
B = int(input("masukkan populasi serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))
for n in range (1, jumlah_hari+1):
    if n % 2 == 0:
        A -= int(A*0.2)
        B -= int(B*0.4)
    else:
        A += int(A*0.3)
        B += int(B*0.5) 
    if n % 5 == 0:
        A -= int(A * 0.10)
        B -= int(B * 0.10)
        print(f"Hari {n} : Predator makan 10% ")

    print(f"Hari {n}: Serangga A = {A}, Serangga B = {B}") 

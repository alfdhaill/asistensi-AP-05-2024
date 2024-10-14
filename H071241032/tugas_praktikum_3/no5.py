populasi_a = int(input("Masukkan populasi awal serangga A: "))
populasi_b = int(input("Masukkan populasi awal serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

for i in range(1, jumlah_hari + 1):
    if i % 2 == 1:
        populasi_a = int(populasi_a + populasi_a * 0.3)  
        populasi_b = int(populasi_b + populasi_b * 0.5)  
    else:
        populasi_a = int(populasi_a - populasi_a * 0.2)  
        populasi_b = int(populasi_b - populasi_b * 0.4)  

    if i % 5 == 0:
        populasi_a = int(populasi_a - populasi_a * 0.1)
        populasi_b = int(populasi_b - populasi_b * 0.1)
        print(f"Hari {i}: predator memakan 10% populasi")

    print(f"Hari {i}: serangga A = {populasi_a}, serangga B = {populasi_b}")

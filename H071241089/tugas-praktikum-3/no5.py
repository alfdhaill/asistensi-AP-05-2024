try:
    serangga_A = int(input("Masukkan populasi awal Serangga A : "))
    serangga_B = int(input("Masukkan populasi awal Serangga B : "))
    hari = int(input("Masukkan jumlah hari : "))

    for i in range(1, hari + 1):
        if i % 2 == 0:
            serangga_A = int(serangga_A * 0.8)
            serangga_B = int(serangga_B * 0.6)
        else:
            serangga_A = int(serangga_A * 1.3)
            serangga_B = int(serangga_B * 1.5)

        if i % 5 == 0:
            print(f"Hari {i}: Predator memakan 10% populasi")

            serangga_A = int(serangga_A * 0.9)
            serangga_B = int(serangga_B * 0.9)

        print(f'Hari {i}: Serangga A = {serangga_A}, Serangga B = {serangga_B}')
except ValueError:
    print("Mohon input angka")

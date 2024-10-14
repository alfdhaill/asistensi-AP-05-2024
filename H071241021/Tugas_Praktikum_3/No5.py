try:
    PopulasiAwalA = int(input('Masukkan populasi awal serangga A : '))
    PopulasiAwalB = int(input('Masukkan populasi awal serangga B : '))
    JumlahHari = int(input('Masukkan jumlah hari :'))

    SeranggaA = PopulasiAwalA
    SeranggaB = PopulasiAwalB

    for hari in range (1, JumlahHari+1):
        if hari % 2 != 0:
            SeranggaA = int(SeranggaA) * 1.3
            SeranggaB = int(SeranggaB) * 1.5
        else:
            SeranggaA = int(SeranggaA) * 0.8
            SeranggaB = int(SeranggaB) * 0.6
        if hari % 5 == 0:
            print (f'Hari {hari}: Predator memakan 10% populasi.')
            SeranggaA = int(SeranggaA) * 0.9
            SeranggaB = int(SeranggaB) * 0.9

        print(f'Hari {hari}: Serangga A = {SeranggaA:.0f}, Serangga B = {SeranggaB:.0f}')
except:
    print ('Masukkan Angka')
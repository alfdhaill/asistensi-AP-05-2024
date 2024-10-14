serangga_a = int(input('Masukkan populasi awal serangga A: '))
serangga_b = int(input('Masukkan populasi awal serangga B: '))
Jumlah_hari = int(input('Masukkan jumlah hari: '))

for i in range(1, Jumlah_hari + 1, 1):
    
    if  i % 2 == 1 :
        
        if i % 5 == 0:  
            serangga_a = int(serangga_a * 1.3)
            serangga_b = int(serangga_b * 1.5)
            serangga_a = int(serangga_a * 0.9)  
            serangga_b = int(serangga_b * 0.9)  
            print('predator memakan 10% populasi')
            print(f'Hari ke {i}:  serangga A: {serangga_a} serangga B: {serangga_b}')
        else:
            serangga_a = int(serangga_a * 1.3)
            serangga_b = int(serangga_b * 1.5)
            print(f'Hari ke {i}: serangga A: {serangga_a} serangga B: {serangga_b}')
        
    if i % 2 == 0 :

        if i % 5 == 0:  
            erangga_a = int(serangga_a* 0.8)
            serangga_b = int(serangga_b* 0.6)
            serangga_a = int(serangga_a * 0.9)  
            serangga_b = int(serangga_b * 0.9)  
            print('predator memakan 10% populasi')
            print(f'Hari ke {i}:  serangga A: {serangga_a} serangga B: {serangga_b}')
        else:
            serangga_a = int(serangga_a* 0.8)
            serangga_b = int(serangga_b* 0.6)
            print(f'Hari ke {i}: serangga A: {serangga_a} serangga B: {serangga_b}')
        
    
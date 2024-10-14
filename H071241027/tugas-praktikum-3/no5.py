popA = int(input("Masukkan populasi awal Serangga A: "))
popB = int(input("Masukkan populasi awal Serangga B: "))
N = int(input("Masukkan jumlah hari: "))    

for hari in range(1, N + 1):    
        if hari % 2 == 1:
            popA = int(1.3 * popA)  
            popB = int(1.5 * popB)  
            print(f"Hari {hari}: Serangga A = {int(popA)}, Serangga B = {int(popB)}")
        else:
            popA = int(0.8 * popA)  
            popB = int(0.6 * popB)
            print(f"Hari {hari} Serangga A = {int(popA)}, Serangga B = {int(popB)}")

        if hari % 5 == 0:
            print(f"Hari {hari}: Predator memakan 10% populasi")
            
            popA = popA * 0.9 
            popB = popB * 0.9  
            print(f"Hari {hari}: Populasi A = {int(popA)}, Populasi B = {int(popB)}")






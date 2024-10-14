populasi1 = int(input(" masukkan populasi awal serangga A :"))
populasi2 = int(input(" masukkan populasi awal serangga B : "))
hari      = int (input(" masukkan jumlah hari : "))

for hari in range (1, hari + 1 ) : 
    if hari % 2 == 1 :
        populasi1 = int(populasi1 * 1.3 )# 30%
        populasi2 = int(populasi2 * 1.5) # penambahan 50%
    else: 
        populasi1 = int(populasi1*0.8) # penurunan 20%
        populasi2 = int(populasi2*0.6) # penurunan 40%

    if hari % 5 == 0 : 
        populasi1  = int(populasi1*0.9)# predator memakan 10%
        populasi2  = int(populasi2*0.9)  
        print(f"Hari {hari}: predator memakan 10% populasi.")
    print(f"hari {hari}: serangga A = {populasi1}, serangga B = {populasi2}")
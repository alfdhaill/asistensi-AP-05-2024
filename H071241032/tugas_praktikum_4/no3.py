def langkah_permainan():
    try:
        n = int(input("Masukkan bilangan bulat positif: "))
        if n <= 0:
            print("Input tidak Valid")
            return
        langkah = 0 #akan terus bertambah sampai nilai hasil_langkah menjadi 1
        hasil_langkah = [] #nilai hasil langkah akan dimasukkan ke dalam sini. 
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
            hasil_langkah.append(n)  
            langkah += 1

        print("Langkah-langkah:")
        for langkah in hasil_langkah:
            print(langkah)  
        
        print(f"Jumlah langkah: {len(hasil_langkah)}")  
    except ValueError:
        print("Input tidak Valid")

langkah_permainan()

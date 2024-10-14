def langkah():
    jarak = 0  
    ada_bahaya = False 
    while True:
        try:
            langkah = int(input("Masukkan jumlah langkah (0 untuk selesai) = "))
            if langkah < 0:
                print("Langkah tidak boleh kurang dari 1") 
                continue 
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar.")
            continue  

        if langkah == 0:
            print("Permainan selesai.")
            if jarak == 50:
                print("Ada harta karun.")
                if not ada_bahaya:
                    print("Kamu dapat menggali.")
                else:
                    print("Namun, ada bahaya! Tidak aman untuk menggali harta karun.")
            elif jarak > 50:
                print("Ada bahaya! Tidak aman untuk menggali harta karun, coba lagi.")
            break

        jarak += langkah

        if langkah > 20:
            ada_bahaya = True
        #     print("Ada bahaya dan tidak ada harta.")
        # else:
        #     print("Tidak ada bahaya dan harta, lanjutkan berjalan.")

    print(f"Total jarak yang telah ditempuh: {jarak} meter.")      

langkah()


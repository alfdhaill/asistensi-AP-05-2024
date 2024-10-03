try:
    populasi_a = float(input("Masukkan populasi awal Serangga A: "))
    populasi_b = float(input("Masukkan populasi awal Serangga B: "))
    hari = int(input("Masukkan jumlah hari untuk prediksi: "))
      
    for day in range(1, hari + 1):
        if day % 2 == 1:  # Hari ganjil
            populasi_a *= 1.3  # Pertambahan 30%
            populasi_b *= 1.5  # Pertambahan 50%
        else:  # Hari genap
            populasi_a *= 0.8  # Penurunan 20%
            populasi_b *= 0.6  # Penurunan 40%

        if day % 5 == 0:  # Setiap kelipatan 5 hari
            print("Predator memakan 10% populasi")
            populasi_a -= populasi_a * 0.1
            populasi_b -= populasi_b * 0.1

            # total_populasi = populasi_a + populasi_b
        
        
        print(f"Hari {day}: Serangga A = {populasi_a:.0f}, Serangga B = {populasi_b:.0f}")

except:
    print("Masukkan angka yang valid.")

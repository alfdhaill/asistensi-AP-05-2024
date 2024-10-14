
    # Input harga saham kemarin
previous_price = float(input("Masukkan harga saham kemarin: "))
    # Harga saham hari ini
current_price = 105.0
    
    # Hitung perubahan persentase harga
percentage_change = ((current_price - previous_price) / previous_price) * 100
    
beli = (percentage_change > 5)
jual = (percentage_change < -3 )
tahan = (percentage_change <= 5) * (percentage_change >= -3)
    # Dapatkan rekomendasi berdasarkan perubahan persentase harga
recommendation = beli * "Beli" + jual * "Jual" + tahan * "Tahan"
    
    # Tampilkan hasil
print(f"Perubahan persentase harga saham adalah {percentage_change:.2f}%")
    
print(f"Rekomendasi investasi: {recommendation}")

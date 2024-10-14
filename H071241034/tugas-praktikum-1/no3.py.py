print ('konversi detik ke jam')
total_seconds = int(input("Masukkan jumlah detik: "))
hours = total_seconds // 3600
minutes = (total_seconds  % 3600) // 60
seconds = total_seconds  % 60
    
time_formatted = f"{hours}:{minutes:02}:{seconds:02}"
print ('konversi detik ke jam')
print(time_formatted)
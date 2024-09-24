print ('Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit')
Celcius = float(input('Masukkan Suhu dalam Celcius :' ))

Kelvin = int( Celcius + 273.15 )
Reamur = int( Celcius * (4/5) )
Fahrenheit = int( Celcius * 9/5 + 32)

print (f'Hasil Konversi dari Suhu {Celcius} ke Kelvin adalah : {Kelvin}K')
print (f'Hasil Konversi dari Suhu {Celcius} ke Reamur adalah : {Reamur}R')
print (f'Hasil Konversi dari Suhu {Celcius} ke Fahrenheit adalah : {Fahrenheit}F')

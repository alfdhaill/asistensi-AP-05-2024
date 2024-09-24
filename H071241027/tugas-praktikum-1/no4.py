print("Konversi Suhu dari Celcius ke Kelvin, reamur dan Fahrenhait")
celsius = float(input("Masukkan suhu dalam Celsius: "))

kelvin = celsius + 273.15
reamur = celsius * 4/5
fahrenheit = celsius * 9/5 + 32

print(f"Hasil konversi dari suhu {celsius} derajat celcius ke Kelvin adalah : {kelvin:.0f} K")
print(f"Hasil konversi dari suhu {celsius} derajat celcius ke Reamur adalah : {reamur:.0f} °Re")
print(f"Hasil konversi dari suhu {celsius} derajat celcius ke Fahrenhait adalah: {fahrenheit:.0f} °F")

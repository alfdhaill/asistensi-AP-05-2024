print("Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit")
celcius = float(input("Masukkan Suhu dalam Celcius : "))

kelvin = celcius + 273
reamur = celcius * 4 // 5
fahrenheit = ((9 * celcius) // 5) + 32

print(
    f"Hasil konversi dari suhu {celcius} derajat Celcius ke Kelvin adalah : {kelvin}K")
print(
    f"Hasil konversi dari suhu {celcius} derajat Celcius ke Reamur adalah : {reamur}R")
print(
    f"Hasil konversi dari suhu {celcius} derajat Celcius ke Fahrenheit adalah : {fahrenheit}F")

print("## Program Konversi Suhu ##")
print("===========================")
print()
print ("konversi suhu dari celcius ke kelvin, reamur dan fahrenheit")

celcius = float(input("Masukkan Suhu Celcius : "))

kelvin = int(celcius + 273.15)
reamur = int(celcius * (4/5))
fahrenheit = int((9/5 * celcius) + 32)

print(f"hasil konversi dari suhu {celcius} derajat celcius ke kelvin adalah : {kelvin}k")
print(f"hasil konversi dari suhu {celcius} derajat celcius ke reamur adalah : {reamur}R")
print(f"hasil konversi dari suhu {celcius} derajat celcius ke fahrenheit adalah : {fahrenheit}F")
print('konversi suhudari celcius ke kelvin, reamur dan fahrenheit')
suhu = float(input('masukkan suhu dalam celcius: '))
kelvin = suhu + 273.15
reamur = (4 / 5) * suhu
fahrenheit = ((9/5) * suhu) + 32
print(f'hasil konversi dari suhu {suhu} derajat celcius ke kelvin adalah: {kelvin}K ')
print(f'hasil konversi dari suhu {suhu} derajat celcius ke reamur adalah: {reamur}R ')
print(f'hasil konversi dari suhu {suhu} derajat celcius ke kelvin adalah: {fahrenheit}F ')
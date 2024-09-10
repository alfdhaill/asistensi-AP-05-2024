print ("konversi suhu dari celcius ke kelvin, reamur dan fahrenheit")
celsius = float(input("Masukkan suhu dalam Celsius: "))
kelvin = celsius + 273.15
reamur = (4/5) * celsius
fahrenheit = (9/5) * celsius + 32


    
print(f"hasil konversi dari Suhu {celsius} Celsius dalam Kelvin: {kelvin:.2f} K")
print(f"hasil konversi dari Suhu {celsius} Celsius dalam Reamur: {reamur:.2f} °Re")
print(f"hasil konversi dari Suhu {celsius} Celsius dalam Fahrenheit: {fahrenheit:.2f} °F")


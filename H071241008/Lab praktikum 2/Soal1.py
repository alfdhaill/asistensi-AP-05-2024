a = int(input('masukkan panjang sisi pertama: '))
b = int(input('masukkan panjang sisi kedua: '))
c = int(input('masukkan sisi ketiga: '))

if a + b > c and  c + a > b and b + c > a :
    if  a==b==c:
        print('segitiga sama sisi')
    elif a==b or b==c or c==a:
        print('segitiga sama kaki')
    else:
        print('segitiga sembarang')
else: 
    print('tidak membentuk segitiga yang valid')
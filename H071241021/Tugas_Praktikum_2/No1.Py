Sisi1 = int(input('masukkan panjang sisi pertama :'))
Sisi2 = int(input('masukkan panjang sisi kedua :'))
Sisi3 = int(input('masukkan panjang sisi ketiga :'))

if Sisi1 + Sisi2 > Sisi3 and Sisi1 + Sisi3 > Sisi2 and Sisi2 + Sisi3 > Sisi1:
    if Sisi1 == Sisi2 == Sisi3:
        segitiga = 'Segitiga Sama Sisi'
    elif Sisi1 != Sisi2 == Sisi3:
        segitiga = 'Segitiga Sama Kaki'
    elif Sisi1 == Sisi2 != Sisi3:
        segitiga = 'Segitiga Sama Kaki'
    elif Sisi1 == Sisi3 != Sisi2:
        segitiga = 'Segitiga Sama Kaki'
    else:
        segitiga = 'Segitiga Sembarang'
else:
    segitiga = 'Tidak Dapat Membentuk Segitiga Yang Valid'

print (f'{segitiga}')
    
        
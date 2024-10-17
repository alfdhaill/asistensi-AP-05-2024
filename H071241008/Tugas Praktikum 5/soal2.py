
def akronim(kalimat):
    return''.join([kata[0]for kata in kalimat.split()])
input_kalimat = input('masukkan kata: ')
hasil = akronim(input_kalimat)
print(hasil)
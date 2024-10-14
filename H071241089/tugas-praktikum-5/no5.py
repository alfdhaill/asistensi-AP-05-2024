import string

hurufKecil = list(string.ascii_lowercase)  
hurufKapital = list(string.ascii_uppercase)  

def periksaKarakterSpesial(karakter):
  karakterSpesial = ["%", "$", "*", "#", "@", "()", "(", ")","!", "^", "&", ",", "-", ".", "[", "}"]
  if karakter in karakterSpesial:
    return True
  return False

stringInput = input("Masukkan String : ")
pergeseran = int(input("Masukkan Jumlah Pergeseran : "))

huruf = []
selainHuruf = []


for i in stringInput:
  if i.isdecimal() or periksaKarakterSpesial(karakter=i):
    selainHuruf.append(i)
  else:
    if i.isupper():
      idx = hurufKapital.index(i)
      idxBaru = idx + pergeseran
      if idxBaru > len(hurufKapital):
        selisih = len(hurufKapital) - idx
        huruf.append(hurufKapital[pergeseran - selisih])
      else: 
        huruf.append(hurufKapital[idx + pergeseran])
    else:
      idx = hurufKecil.index(i)
      idxBaru = idx + pergeseran
      if idxBaru > len(hurufKecil):
        selisih = len(hurufKecil) - idx
        huruf.append(hurufKecil[pergeseran - selisih])
      else: 
        huruf.append(hurufKecil[idx + pergeseran])

outputStr = "".join(huruf) + "".join(selainHuruf)  

print("Text:", stringInput)
print("Shift:", pergeseran)
print("Cipher:", outputStr)
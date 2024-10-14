def getHurufString(dataString):
  dictString = {}
  for kata in dataString:
    if kata in dictString:
      dictString[kata] += 1
    else:
      dictString[kata] = 1

  return dictString

stringPertama = input("Masukkan string pertama: ")
stringKedua = input("Masukkan string kedua: ")

dictStringPertama = getHurufString(stringPertama)
dictStringKedua  = getHurufString(stringKedua)

if dictStringPertama == dictStringKedua:
  print("Jumlah minimum penghapusan untuk membuat anagram: 0")
else:
  penghapusan = 0
  for temp in dictStringPertama:
    if temp in dictStringKedua: # jika huruf dari dictionary string pertama terdapat dalam dictionary string kedua
      # untuk menghindari penjumlahan negatif maka kita lihat mana huruf terbanyak
      if dictStringPertama[temp] > dictStringKedua[temp]:
        penghapusan += dictStringPertama[temp] - dictStringKedua[temp]
      elif dictStringPertama[temp] < dictStringKedua[temp]:
        penghapusan += dictStringKedua[temp] - dictStringPertama[temp]
    else: 
      # jika huruf tidak terdapat pada string kedua maka jumlahkan penghapusan dengan jumlah huruf 
      penghapusan += dictStringPertama[temp]
      
  print("Jumlah minimum penghapusan untuk membuat anagram: ", penghapusan)    

def acronym(kata: str):
  temp = kata.title()
  akronimKata = ""

  for huruf in temp:
    if huruf.isupper():
      akronimKata += huruf

  print(akronimKata)

inputKata = input("Input Kata : ")

acronym(inputKata)

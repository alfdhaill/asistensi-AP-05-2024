def palindrome(kata: str):
  lowerCaseKata = kata.lower()
  reversedKata = "".join(reversed(lowerCaseKata))
  if lowerCaseKata == reversedKata:
    print("Palindrome")
  else:
    print("Not Palindrome")

inputKata = input("Input Kata : ")

palindrome(inputKata)

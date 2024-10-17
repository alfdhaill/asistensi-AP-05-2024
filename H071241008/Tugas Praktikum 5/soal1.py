def Palindrome(string):

    string = string.lower()

    ripersString = string[::-1]

    if string == ripersString:
        print('Palindrome')
    else:
        print('not palindrome')
    
imputan = input('Masukkan kata: ')
Palindrome(imputan)
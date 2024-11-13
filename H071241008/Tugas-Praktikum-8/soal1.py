import re

def string(strings):
    if len(strings) != 45:
        return False
    
    pattern = r'[a-zA-Z2468]{40}+[13579]{5}$'
    if re.match(pattern, strings):
        return False
    
    return True
    
    

inputan = input("masukkan karakter 45: ")
print(string(inputan))

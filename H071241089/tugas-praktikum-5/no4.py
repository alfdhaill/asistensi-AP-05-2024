def print_pattern(word):
    for i in range(len(word)):
        print(word[i])
    
    for i in range(1, len(word)):
        for j in range(len(word) - i):
            print(word[j:j+i+1])

kata = input("Input your string : ")
print("====================")

print_pattern(kata)

import itertools
def semua_substring_v3(s):
    
    # for i, j in itertools.combinations(range(len(s) + 1), 2):
    #     print(s[i:j])
    for i in range (1, len(s) + 1):
        for j in range (len(s) - i + 1):
            k = j + i - 1
            for a in range (j, k + 1):
                print(s[a], end = '')
            print()
string = input('Input your string: ')
semua_substring_v3(string)
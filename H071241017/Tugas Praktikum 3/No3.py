N = int(input("N = "))
M = int(input("M = "))

for i in range(N):
    if i % 2 == 0:
         for j in range(M):
            print(f'Move to ({i},{j})')
    else:
        for j in range(M-1,-1,-1): 
            print(f'MOVE to ({i},{j})') 
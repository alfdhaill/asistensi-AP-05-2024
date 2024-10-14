N = int(input('N = '))
M = int(input('M = '))

for x in range(N):
    if x % 2 == 0:
        for y in range(M):
            print(f'MOVE to ({x}, {y})')
    else:
        for y in range(M - 1, -1, -1):
            print(f'MOVE to ({x}, {y})')

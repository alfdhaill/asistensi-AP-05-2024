N = int(input("N = "))
M = int(input("M = "))

for i in range(abs(N)):
    if i % 2 == 0:
        for j in range(abs(M)):
            print(f"MOVE to ({i},{j})")
    else:
        for j in range(abs(M) -1, -1, -1):
            print(f"MOVE to ({i},{j})")
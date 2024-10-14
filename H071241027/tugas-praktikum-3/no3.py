N = int(input("Masukkan jumlah baris (N): "))
M = int(input("Masukkan jumlah kolom (M): "))

for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            print(f"MOVE to ({i},{j})")
    else:
        for j in range(M-1, -1, -1):
            print(f"MOVE to ({i},{j})")
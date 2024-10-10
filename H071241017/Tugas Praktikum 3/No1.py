n = int(input("Masukkan Jumlah Baris: "))
if n%2 ==0:
    for i in range(1,n//2+1):
        print(" "*(n//2-i)+"*"*(2*i-1))
    for i in range(n//2,0,-1):
        print(" "*(n//2-i)+"*"*(2*i-1))
if n%2 ==1:
    for i in range(1,n//2+2):
        print(" "*(n//2-i+1)+"*"*(2*i-1))
    for i in range(n//2,0,-1):
        print(" "*(n//2-i+1)+"*"*(2*i-1)) 
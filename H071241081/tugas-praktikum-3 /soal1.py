try :
    n = int(input("Masukkan jumlah baris yang anda inginkan : "))
    if n < 0 :
        n = int(input("Masukkan angka diatas 0 : "))
    elif n==1 or n==2 or n== 0:
        print("Angka tidak valid!")
        n = int(input("Masukkan angka selain angka tersebut : "))
    for x in range(1,(n + 2)//2):
        print("  " * (n-x) + "* " * (2*x-1))
    for x in range(((n+1)//2),0,-1):
        print("  " * (n-x) + "* " * (2*x-1))
except:
    print("Harap memasukkan sebuah angka")

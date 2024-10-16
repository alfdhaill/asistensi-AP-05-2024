try :
    n = int (input ("masukan nilai :"))
    if n < 0 :
        n= int (input("masukkan nilai lebih dari nol  :"))
    elif n==1 or n==2 :
        print (" angka tidka valid")
        n = int (input("Angka tidak valid, masukkan angka lain :"))
    for x in range (1,(n+2)//2) :
        print ("  ")* (n-x)+ "* "* (2*x-1)
    for x in range ((n+1)//2,0,-1) :
        print ("  ")*(n-x)+ "* " *(2*x-1)

except:
    print ('Harap masukkan angka')
    
    

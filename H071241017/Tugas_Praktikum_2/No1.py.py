#soal 1
a = int(input("masukan panjang sisi a : "))
b = int(input("masukan panjang sisi b : "))
c = int(input("masukan panjang sisi c : "))
if a + b > c and a + c > b and b + c > a :
    if a == b == c:
        print("segitiga sama sisi")
    elif a == b or b == c or c == a:
        print("segitiga sama kaki")
    elif a != b != c:
        print("segitiga sembarang ")

else :
    print("tidak membentuk segitiga yag valid") 

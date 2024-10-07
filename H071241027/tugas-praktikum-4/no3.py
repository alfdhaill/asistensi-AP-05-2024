

def langkahkaki(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            # print(f"{n // 2:.1f}")
            n //= 2
            print(f"{n}")
        else:
            # print(f"{3 * n + 1:.1f}")
            n = 3 * n + 1
            print(f"{n}")
        steps += 1
    return steps

def main():
    try:
        n = int(input("Masukkan bilangan bulat positif: "))
        if n <= 0:
            print("Input tidak Valid")
        else:
            steps = langkahkaki(n)
            print(f"Jumlah langkah: {steps}")
    except ValueError:
        print("Input tidak Valid")

main()
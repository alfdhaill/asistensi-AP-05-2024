import random

def hitung_nilai(kartu):
    total = 0
    ace_count = 0
    for k in kartu:
        if k == 1:  
            ace_count += 1
            total += 11
        elif k > 10:  
            total += 10
        else:
            total += k

    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1

    return total

def ambil_kartu():
    return random.randint(1, 11)

def blackjack():
    print("Welcome to Blackjack!")
    
    kartu_pemain = [ambil_kartu()]
    kartu_dealer = [ambil_kartu()]
    
    print(f"Kartu anda: {hitung_nilai(kartu_pemain)}")

    while True:
        ambil = input("Ambil kartu lagi? (y/n): ").lower()
        if ambil == 'y':
            kartu_pemain.append(ambil_kartu())
            total_pemain = hitung_nilai(kartu_pemain)
            print(f"Kartu anda: {total_pemain}")

            if total_pemain > 21:
                print("Anda kalah, kartu melebihi 21.")
                return
        elif ambil == 'n':
            break
        
        elif ambil !='y'or'n':
            print("Input tidak valid. Masukkan (y/n)")
            return

    print(f"Kartu dealer: {hitung_nilai(kartu_dealer)}")
    while hitung_nilai(kartu_dealer) < 17:
        kartu_dealer.append(ambil_kartu())
        print(f"Kartu dealer sekarang: {hitung_nilai(kartu_dealer)}")

    total_pemain = hitung_nilai(kartu_pemain)
    total_dealer = hitung_nilai(kartu_dealer)

    if total_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif total_pemain > total_dealer:
        print("Anda menang!")
    elif total_pemain == total_dealer:
        print("Seri!")
    else:
        print("Dealer menang!")

blackjack()

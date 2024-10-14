import random
def acak_kartu():
    return random.randint(1, 11)
def mainkan_pemain(total):
    while True:
        ambil = input("Ambil kartu? (y/n): ")
        if ambil == 'y':
            total += acak_kartu()  
            print(f"Kartu anda: {total}")
            if total > 21:
                print("Kalah! Kartu lebih dari 21.")
                return total 
        elif ambil == 'n':
            return total 
        else:
            print("Pilih y atau n")
def mainkan_dealer(total):
    while total < 17:
        total += acak_kartu()  
    return total
def blackjack():
    print("Selamat datang di Blackjack!")
    total_pemain = acak_kartu()  
    total_dealer = acak_kartu()  
    print(f"Kartu anda: {total_pemain}")
    total_pemain = mainkan_pemain(total_pemain)
    if total_pemain > 21:
        return
    total_dealer = mainkan_dealer(total_dealer)
    
    print(f"Kartu akhir anda: {total_pemain}")
    print(f"Kartu akhir dealer: {total_dealer}")
    
    if total_dealer > 21:
        print("menang")
    elif total_pemain > total_dealer:
        print("congrats")
    elif total_pemain < total_dealer:
        print("nt nt")
    else:
        print("Seri!")
blackjack()

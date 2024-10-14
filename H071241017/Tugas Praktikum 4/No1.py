import random as rn
kartu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def ambil_kartu():
    return rn.choice(kartu) 
def blackjack():
    kartu_pemain = [ambil_kartu()]
    kartu_dealer = [ambil_kartu()]
    print(f"Kartu anda sekarang adalah : {kartu_pemain[0]}") 
    while True:
        input_pemain = input("Ingin mengambil kartu lagi? (ya/tidak): ").lower() 
        if input_pemain == "ya":
            kartu_pemain.append(ambil_kartu())
            print(f"Kartu anda sekarang adalah {sum(kartu_pemain)}")  
            if sum(kartu_pemain) > 21:
                print("Anda kalah Total kartu lebih dari 21.")
                return
        elif input_pemain == "tidak" :
            break
        else : 
            print("input tidak valid, masukan ya atau tidak.") 
    while sum(kartu_dealer) < 17:
        kartu_dealer.append(ambil_kartu())
        print(f"Kartu dealer sekarang adalah {sum(kartu_dealer)}") 
    total_pemain = sum(kartu_pemain)
    total_dealer = sum(kartu_dealer)
    if total_dealer > 21:
        print("Dealer melebihi 21 Anda menang")
    elif total_pemain > total_dealer:
        print(f"Anda menang, Kartu Anda {total_pemain}, kartu dealer {total_dealer}.")
    elif total_pemain < total_dealer:
        print(f"Anda kalah, Kartu Anda {total_pemain}, kartu dealer {total_dealer}.")
    elif total_dealer == total_pemain:
        print(f"Permainan seri, Kartu Anda {total_pemain}, kartu dealer {total_dealer}.")
print("welcome to blackjack")
blackjack()

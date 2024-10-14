import random

def acakan_maut():
    return random.randint(1, 11)

def korban_turn():
    total_si_korban = acakan_maut()
    print(f"Kartu anda sekarang adalah: {total_si_korban}")
    
    while True:
        keputusan = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if keputusan == 'y':
            kartu_baru = acakan_maut()
            total_si_korban += kartu_baru
            print(f"Kartu anda sekarang adalah: {total_si_korban}")
            if total_si_korban > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return total_si_korban
        elif keputusan == 'n':
            break
    return total_si_korban

def yang_membodohi_turn():
    total_yang_membodohi = acakan_maut()
    print(f"Kartu dealer adalah: {total_yang_membodohi}")
    
    while total_yang_membodohi < 17:
        kartu_baru = acakan_maut()
        total_yang_membodohi += kartu_baru
        print(f"Kartu dealer sekarang adalah: {total_yang_membodohi}")
    
    return total_yang_membodohi

def blackjack_game():
    print("Welcome to Blackjack!")
    
    total_si_korban = korban_turn()
    if total_si_korban > 21:
        return
    
    total_yang_membodohi = yang_membodohi_turn()
    
    if total_yang_membodohi > 21:
        print("Anda menang, dealer melebihi 21.")
    elif total_si_korban > total_yang_membodohi:
        print("Anda menang!")
    elif total_si_korban == total_yang_membodohi:
        print("Seri!")
    else:
        print("Dealer menang!")

blackjack_game()

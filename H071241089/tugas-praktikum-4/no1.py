import random


def getRandomCard(a, b):
    return random.randint(a, b)


print("Welcome to Blackjack!")


def giliranPlayer():
    jumlahKartu = 0

    response = ["y", "Y", "n", "N"]

    while True:
        kartuPemain = getRandomCard(1, 11)
        jumlahKartu += kartuPemain

        print(f"Kartu anda sekarang adalah: {jumlahKartu}")

        if jumlahKartu > 21:
            return jumlahKartu

        konfirmasi = input("Apakah masih akan mengambil kartu? (y/n) ")

        if konfirmasi not in response:
            return "Input tidak valid"
            break

        if konfirmasi == "n" or konfirmasi == "N":
            return jumlahKartu


def giliranDealer():
    kartuDealer = getRandomCard(1, 11)
    while kartuDealer <= 17:
        nomorRandom = getRandomCard(1, 11)
        kartuDealer += nomorRandom
        print(f"Kartu dealer adalah : {kartuDealer}")

    return kartuDealer


def tentukanPemenang(kartuPlayer, kartuDealer):
    if kartuDealer > 21:
        print("Anda menang!")
    else:
        if kartuDealer > kartuPlayer:
            print("Anda kalah!")
        elif kartuPlayer > kartuDealer:
            print("Anda menang!")
        elif kartuPlayer == kartuDealer:
            print("Seri!")


jumlahKartuPlayer = giliranPlayer()

if type(jumlahKartuPlayer) == str:
    print(jumlahKartuPlayer)
elif jumlahKartuPlayer > 21:
    print("Anda kalah!")
else:
    jumlahKartuDealer = giliranDealer()

    tentukanPemenang(jumlahKartuPlayer, jumlahKartuDealer)

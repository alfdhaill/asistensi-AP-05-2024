# nomor 2
# def one_piece():
#     sunnyGo = 0
#     yang_aman_aman_aja = 20
#     laughtale = 50
#     while True :
#         try:
#             sea = int(input('Masukkan jumlah jarak(meter): '))
#             if sea <= 0 :
#                 print('Kamu menyelesaikan permainannya')
#                 if sunnyGo == laughtale :
#                     print('Aman! Kamu tepat dan mendapatkan harta karunnya')
#                 else:
#                     print('Tidak aman untuk menggali harta karun coba lagi')
#                 break
        
#             if sea > yang_aman_aman_aja:
#                 print('Tidak aman menggali di sini')
        
#             sunnyGo += sea
#             print(f'Jarak total: {sunnyGo} meter')
        
#             if sunnyGo == laughtale :
#                 print('Aman! Kamu tepat dan mendapatkan harta karunnya')
#                 break
#             elif sunnyGo > laughtale:
#                 print('Kamu melewati harta karun')
#                 break
#         except ValueError:
#             print('Input tidak valid')
# one_piece()
        
# no 4
# print('Selamat datang di kalkulator sederhana!')
# try:
#     a = int(input('Masukkan angka pertama: '))
#     b = int(input('Masukkan angka kedua: '))
#     operasi = input('operasi (+, -, *, //): ')
#     def kalkulator(a, b, operasi):
#         if operasi == '+' :
#             return a + b
#         if operasi == '-' :
#             return a - b
#         if operasi == '*' :
#             return a * b
#         if operasi == '//' :
#             return a // b
#     print(f'hasil: {kalkulator(a, b, operasi)}')

# except : ValueError 
# print()
##no 4
# a = float(input('Masukkan angka pertama: '))
# b = float(input('Masukkan angka kedua: '))
# operasi = input('operasi (+, -, *, //): ')

# if b == 0 and operasi == '/' :
#      print("pembagian dengan nol tidak diperbolehkan")

# # if operasi != ("+", "-", "*", "//") :

# #     print("operasi tidak valid gunakan +, -, *, //")
# if (a or b) == str :
#      print('input tidak valid: could not convert str to int')
# def kalkulator(a, b, operasi):
#         if operasi == '+' :
#             return a + b
#         if operasi == '-' :
#             return a - b
#         if operasi == '*' :
#             return a * b
#         if operasi == '/' :
#             if b == 0 :
#                  return
#             else:
#                 return a / b
        
# print(f'hasil: {kalkulator(a, b, operasi)}')

# no2
def periksa_bahaya(yang_aman_aman_aja):
    if yang_aman_aman_aja > 20:
        return True  
    return False  

def perbarui_jarak(laughtale, sunnygo):
    return laughtale + sunnygo

def cek_status(laughtale):
    if laughtale == 50:  
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
        return True
    elif laughtale > 50:  
        print("Lebih langkahnya paok")
        return True
    return False  

def onePiece():
    laughtale = 0  
    while True:
        try:
            sunnygo = int(input("Masukkan jarak langkah (meter) atau 0 untuk berhenti: "))
        
            if sunnygo <= 0:  
                laughtale = perbarui_jarak(laughtale, sunnygo)  
                print(f"Total jarak: {laughtale} meter")
                print('Ada bahaya: Ya' if periksa_bahaya(laughtale) else 'Ada bahaya: Tidak')
                
                break
                # if periksa_bahaya(laughtale):
                #     print('Ada bahaya: Ya')
                # else:
                #     print('Ada bahaya: Tidak')
                    
            
        
            if periksa_bahaya(sunnygo):  
                print("Tidak aman untuk menggali harta karun. Coba lagi!")
                continue  
        
            # laughtale = perbarui_jarak(laughtale, sunnygo)  
            # print(f"Total jarak: {laughtale} meter")
        
            if cek_status(laughtale):  
                break
        except ValueError :
            print('input tidak valid masukkan bilangan bulat')

onePiece()
#no 3
# def hitung_langkah(s):
#     if not isinstance(s, int) or s <= 0:
#         return "Input tidak Valid"
#     langkah = 0
#     print(f"Langkah ke-{langkah}: {s}")
    
#     while s != 1:
#         if s % 2 == 0:
#             s //= 2
#         else:
#             s = s * 3 + 1
#         langkah += 1
#         print(f"Langkah ke-{langkah}: {s}")
    
#     return (f"Total langkah: {langkah}")

# try:
#     s = int(input("Masukkan bilangan bulat positif: "))
#     print(hitung_langkah(s))
# except ValueError:
#     print("Input tidak Valid")


# import random

# def acakan_maut():
#     return random.randint(1, 11)

# def korban_turn():
#     total_si_korban = acakan_maut()
#     print(f"Kartu anda sekarang adalah: {total_si_korban}")
    
#     while True:
#         keputusan = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
#         if keputusan == 'y':
#             kartu_baru = acakan_maut()
#             total_si_korban += kartu_baru
#             print(f"Kartu anda sekarang adalah: {total_si_korban}")
#             if total_si_korban > 21:
#                 print("Anda kalah, kartu anda melebihi 21.")
#                 return total_si_korban
#         elif keputusan == 'n':
#             break
#     return total_si_korban

# def yang_membodohi_turn():
#     total_yang_membodohi = acakan_maut()
#     print(f"Kartu dealer adalah: {total_yang_membodohi}")
    
#     while total_yang_membodohi < 17:
#         kartu_baru = acakan_maut()
#         total_yang_membodohi += kartu_baru
#         print(f"Kartu dealer sekarang adalah: {total_yang_membodohi}")
    
#     return total_yang_membodohi

# def blackjack_game():
#     print("Welcome to Blackjack!")
    
#     total_si_korban = korban_turn()
#     if total_si_korban > 21:
#         return
    
#     total_yang_membodohi = yang_membodohi_turn()
    
#     if total_yang_membodohi > 21:
#         print("Anda menang, dealer melebihi 21.")
#     elif total_si_korban > total_yang_membodohi:
#         print("Anda menang!")
#     elif total_si_korban == total_yang_membodohi:
#         print("Seri!")
#     else:
#         print("Dealer menang!")

# blackjack_game()

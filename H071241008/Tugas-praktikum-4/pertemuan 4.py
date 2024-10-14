# def tambah (a,b):
#     return (a + b)
# jumlah = tambah(2, 4)
# print(jumlah)
    
# def printhello():
#     print('hello world')
# printhello()

# def add(*args):
#     print(f'{args} brtipe {type(args)})')

# def one_piece():
#     jarakTotal = 0  # Konsisten dengan penulisan variabel
#     yang_aman_aman_aja = 20
#     laughtale = 50
    
#     while True:
#         try:
#             sea = int(input('Masukkan jumlah jarak (meter): '))
            
#             if sea <= 0:
#                 print('Kamu menyelesaikan permainannya')
#                 if jarakTotal == laughtale:
#                     print('Aman! Kamu tepat dan mendapatkan harta karunnya')
#                 else:
#                     print('Tidak aman untuk menggali harta karun coba lagi')
#                 break  # Mengakhiri permainan
            
#             if sea > yang_aman_aman_aja:
#                 print('Tidak aman menggali di sini')
            
#             jarakTotal += sea
#             print(f'Jarak total: {jarakTotal} meter')
            
#             if jarakTotal == laughtale:
#                 print('Aman! Kamu tepat dan mendapatkan harta karunnya')
#                 break
#             elif jarakTotal > laughtale:
#                 print('Kamu melewati harta karun')
#                 break
#         except ValueError:
#             print('Input tidak valid')
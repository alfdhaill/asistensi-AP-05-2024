try :
    total_harga = int (input ('MASUKKAN HARGA YANG HARUS DIBAYAR:'))
    total_uang =int (input ('MASUKKAN UANG YANG DIBERIKAN:'))

    if total_uang<  total_harga :
        print ("TOTAL UANG YANG DIBERIKAN TIDAK CUKUP ")
    elif total_harga < 0 :
        print ("HARGA YAG DIBERIKAN HARUS LEBIH DARI 0")

    kembalian = total_uang - total_harga
    print (f'KEMBALIAN: {kembalian}')

    pecahan = [100000,50000,20000,10000,5000,2000,1000]
    rincian_kembalian = {}

    


    
    
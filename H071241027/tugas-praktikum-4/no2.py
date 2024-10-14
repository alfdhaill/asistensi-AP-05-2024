def main():
    totaljarak = 0
    bahaya = False

    while True:
        try:
            langkah = int(input("Masukkan jarak langkah yang ditempuh dalam meter (atau 0 untuk berhenti): "))

            if langkah< 0:
                print("Input tidak valid. Masukkan bilangan bulat.")
                continue

            if langkah == 0:
                break

            if langkah > 20:
                bahaya = True
   

        except ValueError:
            print("Input tidak valid, masukkan bilangan bulat")
            
        totaljarak += langkah

    if bahaya:
        print(f"Total jarak: {totaljarak} meter")
        print("Ada bahaya : Ya")
        print("Keputusan : Tidak aman untuk menggali harta karun. Coba lagi!")
    elif totaljarak == 50:
        print(f"Total jarak: {totaljarak} meter")
        print("Ada bahaya : Tidak")
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print(f"Totak jarak : {totaljarak} meter")
        print("Tidak menemukan harta karun. Coba lagi!")

main()

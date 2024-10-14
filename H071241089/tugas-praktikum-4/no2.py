def getLangkah():
    try:
        langkah = int(
            input("Masukkan langkah (meter) atau 0 untuk selesai: "))

        if langkah < 0:
            raise Exception("Langkah tidak boleh negatif")

        return langkah
    except ValueError:
        print("Input tidak valid. Masukkan bilangan bulat.")
    except Exception as e:
        print(e)

def determineWinner(jumlahLangkah: int, bahaya: bool):
    if jumlahLangkah == 50 and bahaya == False:
        print("Aman! Kamu tepat menemukan harta karung dan menang!")
    elif bahaya:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")


bahaya = False
jumlahLangkah = 0

while True:
    langkah = getLangkah()
    jumlahLangkah += langkah
    if langkah > 20:
        bahaya = True
    elif langkah == 0:
        break

print(f"Total jarak: {jumlahLangkah}")
print("Ada bahaya:", "Ya" if bahaya else "Tidak")

determineWinner(jumlahLangkah, bahaya)

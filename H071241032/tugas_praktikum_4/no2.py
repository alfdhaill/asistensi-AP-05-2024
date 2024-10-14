def hitung_total_jarak():
    total_jarak = 0
    while True:
        langkah = input("Masukkan langkah anda (meter), klik 0 untuk berhenti menggali: ")
        try:
            langkah = int(langkah)
        except ValueError:
            print("angka blok, gimana mau itungnya coba")
            continue
        if langkah < 0:
            print("mundur?")
            break
        if langkah == 0:
            break
        total_jarak += langkah
    return total_jarak
def danger(jarak):
    if jarak > 20:
        return True
    return False
def harta_tahta():
    langkah_anda = hitung_total_jarak()
    bahaya = danger(langkah_anda)
    
    print(f"Total jarak: {langkah_anda} meter")
    print(f"Ada bahaya: {'Ya' if bahaya else 'Tidak'}")

    if langkah_anda == 50 and not bahaya:
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    elif bahaya:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")
harta_tahta()
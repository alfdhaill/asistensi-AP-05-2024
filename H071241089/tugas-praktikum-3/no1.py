baris = int(input("Masukkan Jumlah Baris : "))

setengahKetupat = (baris // 2)
for i in range(1, setengahKetupat + 1):
    spasi = ((setengahKetupat - i) + 1) * 2
    bintang = (2 * i) - 1
    print(" " * spasi + "* " * bintang)

if baris % 2 != 0:
    print(baris * "* ")

for i in range(setengahKetupat, 0, -1):
    spasi = ((setengahKetupat - i) + 1) * 2
    bintang = (2 * i) - 1
    print(" " * spasi + "* " * bintang)

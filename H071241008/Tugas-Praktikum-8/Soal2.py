import re

def check_ip4(ip):
    karakter = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(karakter, ip):
        return True
    return False

def check_ip6(ip):
    oktad = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    oktad_singkat = r'^([0-9a-fA-F]{1,4}:){0,7}(:[0-9a-fA-F]{1,4}){1,7}$'
    if re.match(oktad, ip) or re.match(oktad_singkat, ip):
        return True
    return False

def check_ip_addres(ip_addres):
    hasil = []
    for ip in ip_addres:
        if check_ip4(ip):
            hasil.append("IPv4")
        elif check_ip6(ip):
            hasil.append("IPv6")
        else:
            hasil.append("Bukan IP Address")
    return hasil

n = int(input("Masukkan jumlah IP Address: "))
ip_adres = []

for _ in range(n):
    ip = input("Masukkan IP Address: ").strip()
    ip_adres.append(ip)

hasil = check_ip_addres(n, ip_adres)
for i in hasil:
    print(i)
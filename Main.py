from rumus import BangunDatar, BangunRuang
import os

Clear = lambda: os.system('cls')

# Main
Clear()
print(24*'=')
print('==== Selamat datang ====')
print(24*'=', '\n')

while True:
    print(24*'=')
    print('==\t  Menu' + 8*' ' + "==")
    print(24*'=')

    print('[1] Bangun Datar')
    print('[2] Bangun Ruang')
    print('[99] Keluar')
    print(24*'=')
    pilih = int(input('Masukan pilihan : '))

    if pilih == 1:
        BangunDatar()
    elif pilih == 2:
        BangunRuang()
    elif pilih == 99:
        exit()
    else:
        input('Anda salah memasukan pilihan, silakan ulangi')
    
    Clear()

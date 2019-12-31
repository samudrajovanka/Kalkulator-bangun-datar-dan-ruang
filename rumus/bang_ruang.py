from .ruang import *
import os

Clear = lambda: os.system('cls')

def BangunRuang():
    bangunRuang = ('Kubus', 'Balok', 'Prisma Segitiga', 'Limas Segiempat', 'Limas Segitiga', 'Tabung', 'Kerucut', 'Bola')

    while True:
        Clear()
        print(24*'=')
        print('==    Bangun Datar    ==')
        print(24*'=')
        for nomor, nama in enumerate(bangunRuang):
            nomor += 1
            print('[' + str(nomor) + ']', nama)
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))

        if pilih == 1:
            Kubus()
        elif pilih == 2:
            Balok()
        elif pilih == 3:
            PrismaSegitiga()
        elif pilih == 4:
            LimasSegiempat()
        elif pilih == 5:
            LimasSegitiga()
        elif pilih == 6:
            Tabung()
        elif pilih == 7:
            Kerucut()
        elif pilih == 8:
            Bola()
        elif pilih == 98:
            break
        else:
            input('Anda salah memasukan pilihan, silakan ulangi')
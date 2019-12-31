from .datar import *
import os

Clear = lambda: os.system('cls')

def BangunDatar():
    bangunDatar = ('Persegi', 'Persegi Panjang', 'Segitiga', 'Lingkaran', 'Trapesium', 'Jajar Genjang', 'Layang-Layang', 'Belah Ketupat')

    while True:
        Clear()
        print(24*'=')
        print('==    Bangun Datar    ==')
        print(24*'=')
        for nomor, nama in enumerate(bangunDatar):
            nomor += 1
            print('[' + str(nomor) + ']', nama)
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            Persegi()
        elif pilih == 2:
            PersegiPanjang()
        elif pilih == 3:
            Segitiga()
        elif pilih == 4:
            Lingkaran()
        elif pilih == 5:
            Trapesium()
        elif pilih == 6:
            JajarGenjang()
        elif pilih == 7:
            LayangLayang()
        elif pilih == 8:
            BelahKetupat()
        elif pilih == 98:
            break
        else:
            input('Anda salah memasukan pilihan, silakan ulangi')
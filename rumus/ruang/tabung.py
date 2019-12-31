from ..datar import lingkaran
import os

Clear = lambda: os.system('cls')

def Volume(rAlas, t):
    lLing = lingkaran.Luas(rAlas)
    return lLing*t 

def Luas(rAlas, t):
    lLing = lingkaran.Luas(rAlas)
    lKel = lingkaran.Keliling(rAlas)
    return 2*lLing+lKel*t

def Tabung():
    while True:
        Clear()
        print(24*'=')
        print('==' + 2*' ' + 'Tabung' + 3*' ' + '==')
        print(24*'=')
        print('[1] Volume')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Volume Tabung :\n')
                r = int(input('Masukan jari-jari = '))
                t = int(input('Masukan tinggi    = '))
                print(24*'=')
                volume = Volume(r, t)
                print('Volume =', volume)
                
                while True:
                    ulang = input('Ulangi [y/t] ? ')
                    if ulang == 'y' or ulang == 'Y':
                        break
                    elif ulang == 't' or ulang == 'T':
                        break
                    else:
                        input('Anda salah memasukan pilihan, silakan ulangi')
                if ulang == 't' or ulang == 'T':
                    break
        elif pilih == 2:
            while True:
                Clear()
                print('Luas Tabung :\n')
                r = int(input('Masukan jari-jari = '))
                t = int(input('Masukan tinggi    = '))
                print(24*'=')
                luas = Luas(r, t)
                print('Luas =', luas)
                
                while True:
                    ulang = input('Ulangi [y/t] ? ')
                    if ulang == 'y' or ulang == 'Y':
                        break
                    elif ulang == 't' or ulang == 'T':
                        break
                    else:
                        input('Anda salah memasukan pilihan, silakan ulangi')
                if ulang == 't' or ulang == 'T':
                    break
        elif pilih == 98:
            break
        else:
            input('Anda salah memasukan pilihan, silakan ulangi')
            input()
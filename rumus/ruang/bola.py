from ..datar import lingkaran
import os

Clear = lambda: os.system('cls')

PHI = 3.14

def Volume(r):
    return (4/3)*(PHI*(r**3))

def Luas(r):
    lLing = lingkaran.Luas(r)
    return 4*lLing

def Bola():
    while True:
        Clear()
        print(24*'=')
        print('==' + 2*' ' + 'Bola' + 3*' ' + '==')
        print(24*'=')
        print('[1] Volume')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Volume Bola :\n')
                r = int(input('Masukan jari-jari = '))
                print(24*'=')
                volume = Volume(r)
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
                print('Luas Bola :\n')
                r = int(input('Masukan jari-jari = '))
                print(24*'=')
                luas = Luas(r)
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
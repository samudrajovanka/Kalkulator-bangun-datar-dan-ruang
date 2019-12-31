from ..datar import segitiga
import os

Clear = lambda: os.system('cls')

def Volume(a, tseg, tLim):
    lSeg = segitiga.Luas(a, tseg)
    return (lSeg*tLim)/3

def Luas(sAlas, tAlas, tSel):
    lSegAlas = segitiga.Luas(sAlas, tAlas)
    lSegSel = segitiga.Luas(sAlas, tSel)
    return lSegAlas+lSegSel

def LimasSegitiga():
    while True:
        Clear()
        print(24*'=')
        print('==' + 2*' ' + 'Limas Segitiga' + 3*' ' + '==')
        print(24*'=')
        print('[1] Volume')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Volume Limas Segitiga :\n')
                sAlas = int(input('Masukan sisi alas    = '))
                tAlas = int(input('Masukan tinggi alas  = '))
                tinggiLim = int(input('Masukan tinggi limas = '))
                print(24*'=')
                volume = Volume(sAlas, tAlas, tinggiLim)
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
                print('Luas Limas Segitiga :\n')
                sAlas = int(input('Masukan sisi alas       = '))
                tAlas = int(input('Masukan tinggi alas     = '))
                tinggiSeg = int(input('Masukan tinggi segitiga = '))
                print(24*'=')
                luas = Luas(sAlas, tAlas, tinggiSeg)
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
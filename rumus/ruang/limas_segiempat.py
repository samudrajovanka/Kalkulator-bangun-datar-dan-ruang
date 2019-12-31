from ..datar import persegi, segitiga
import os

Clear = lambda: os.system('cls')

def Volume(s, tLim):
    lPer = persegi.Luas(s)
    return (lPer*tLim)/3

def Luas(s, tSeg):
    lPer = persegi.Luas(s)
    lSeg = segitiga.Luas(s, tSeg)
    return lPer+lSeg

def LimasSegiempat():
    while True:
        Clear()
        print(24*'=')
        print('==' + 2*' ' + 'Limas Segiempat' + 3*' ' + '==')
        print(24*'=')
        print('[1] Volume')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Volume Limas Segiempat :\n')
                sisi = int(input('Masukan sisi alas   = '))
                tinggiLim = int(input('Masukan tinggi limas = '))
                print(24*'=')
                volume = Volume(sisi, tinggiLim)
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
                print('Luas Limas Segiempat :\n')
                sisi = int(input('Masukan sisi alas       = '))
                tinggiSeg = int(input('Masukan tinggi segitiga = '))
                print(24*'=')
                luas = Luas(sisi, tinggiSeg)
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
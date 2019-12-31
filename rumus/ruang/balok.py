import os

Clear = lambda: os.system('cls')

def Volume(p, l, t):
    return p*l*t

def Luas(p, l, t):
    return (2*p*l)+(2*p*t)+(2*l*t)

def Balok():
    while True:
        Clear()
        print(24*'=')
        print('==' + 7*' ' + 'Balok' + 8*' ' + '==')
        print(24*'=')
        print('[1] Volume')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Volume Balok :\n')
                panjang = int(input('Masukan panjang = '))
                lebar = int(input('Masukan lebar   = '))
                tinggi = int(input('Masukan tinggi  = '))
                print(24*'=')
                volume = Volume(panjang, lebar, tinggi)
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
                print('Luas Balok :\n')
                panjang = int(input('Masukan panjang = '))
                lebar = int(input('Masukan lebar   = '))
                tinggi = int(input('Masukan tinggi  = '))
                print(24*'=')
                luas = Luas(panjang, lebar, tinggi)
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
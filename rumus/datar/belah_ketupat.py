import os

Clear = lambda: os.system('cls')

def Keliling(s):
    return 4*s

def Luas(d1, d2):
    return (d1*d2)/2

def BelahKetupat():
    while True:
        Clear()
        print(24*'=')
        print('==' + 3*' ' + 'Belah Ketupat' + 4*' ' + '==')
        print(24*'=')
        print('[1] Keliling')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Keliling Belah Ketupat :\n')
                sisi = int(input('Masukan sisi = '))
                print(24*'=')
                keliling = Keliling(sisi)
                print('Keliling =', keliling)
                
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
                print('Luas Belah Ketupat :\n')
                d1 = int(input('Masukan diagonal 1 = '))
                d2 = int(input('Masukan diagonal 2 = '))
                print(24*'=')
                luas = Luas(d1, d2)
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
import os

Clear = lambda: os.system('cls')

def Keliling(p, l):
    return 2*(p+l)

def Luas(p, l):
    return p*l

def PersegiPanjang():
    while True:
        Clear()
        print(24*'=')
        print('==' + 2*' ' + 'Persegi Panjang' + 3*' ' + '==')
        print(24*'=')
        print('[1] Keliling')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Keliling Persegi Panjang :\n')
                panjang = int(input('Masukan panjang = '))
                lebar = int(input('Masukan lebar   = '))
                print(24*'=')
                keliling = Keliling(panjang, lebar)
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
                print('Luas Persegi Panjang :\n')
                panjang = int(input('Masukan panjang = '))
                lebar = int(input('Masukan lebar   = '))
                print(24*'=')
                luas = Luas(panjang, lebar)
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
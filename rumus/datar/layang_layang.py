import os

Clear = lambda: os.system('cls')

def Keliling(s1, s2):
    return 2*(s1+s2)

def Luas(d1, d2):
    return (d1*d2)/2

def LayangLayang():
    while True:
        Clear()
        print(24*'=')
        print('==' + 3*' ' + 'Layang-Layang' + 4*' ' + '==')
        print(24*'=')
        print('[1] Keliling')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Keliling Layang-Layang :\n')
                sisi1 = int(input('Masukan sisi 1 = '))
                sisi2 = int(input('Masukan sisi 2 = '))
                print(24*'=')
                keliling = Keliling(sisi1, sisi2)
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
                print('Luas Layang-Layang :\n')
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
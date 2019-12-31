import os

Clear = lambda: os.system('cls')

def Keliling(s1, s2, s3):
    return s1+s2+s3

def Luas(a, t):
    return (a*t)/2

def Segitiga():
    while True:
        Clear()
        print(24*'=')
        print('==' + 6*' ' + 'Segitiga' + 6*' ' + '==')
        print(24*'=')
        print('[1] Keliling')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Keliling Segitiga :\n')
                sisi1 = int(input('Masukan sisi 1 = '))
                sisi2 = int(input('Masukan sisi 2 = '))
                sisi3 = int(input('Masukan sisi 3 = '))
                print(24*'=')
                keliling = Keliling(sisi1, sisi2, sisi3)
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
                print('Luas Segitiga :\n')
                alas = int(input('Masukan alas   = '))
                tinggi = int(input('Masukan tinggi   = '))
                print(24*'=')
                luas = Luas(alas, tinggi)
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
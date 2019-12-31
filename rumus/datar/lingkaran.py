import os

Clear = lambda: os.system('cls')

PHI = 3.14

def Keliling(r):
    return PHI*2*r

def Luas(r):
    return PHI*(r**2)

def Lingkaran():
    while True:
        Clear()
        print(24*'=')
        print('==' + 5*' ' + 'Lingkaran' + 6*' ' + '==')
        print(24*'=')
        print('[1] Keliling')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Keliling Lingkaran :\n')
                jariJari = int(input('Masukan jari-jari = '))
                print(24*'=')
                keliling = Keliling(jariJari)
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
                print('Luas Lingkaran :\n')
                jariJari = int(input('Masukan jari-jari = '))
                print(24*'=')
                luas = Luas(jariJari)
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
import os

Clear = lambda: os.system('cls')

def Keliling(s1, s2, s3, s4):
    return s1+s2+s3+s4

def Luas(sisiAtas, sisiBawah, tinggi):
    return ((sisiBawah+sisiAtas)*tinggi)/2

def Trapesium():
    while True:
        Clear()
        print(24*'=')
        print('==' + 5*' ' + 'Trapesium' + 5*' ' + '==')
        print(24*'=')
        print('[1] Keliling')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Keliling Trapesium :\n')
                sisi1 = int(input('Masukan sisi 1 = '))
                sisi2 = int(input('Masukan sisi 2 = '))
                sisi3 = int(input('Masukan sisi 3 = '))
                sisi4 = int(input('Masukan sisi 4 = '))
                print(24*'=')
                keliling = Keliling(sisi1, sisi2, sisi3, sisi4)
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
                print('Luas Trapesium :\n')
                alasAtas = int(input('Masukan alas atas  = '))
                alasBawah = int(input('Masukan alas bawah = '))
                tinggi = int(input('Masukan tinggi    = '))
                print(24*'=')
                luas = Luas(alasAtas, alasBawah, tinggi)
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
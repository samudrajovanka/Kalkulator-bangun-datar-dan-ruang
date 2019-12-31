from ..datar import segitiga
import os

Clear = lambda: os.system('cls')

def Volume(alasSeg, tinggiSeg, tinggiPris):
    lSeg = segitiga.Luas(alasSeg, tinggiSeg)
    return lSeg*tinggiSeg

def Luas(s1, s2, s3, t, alas):
    lSeg = segitiga.Luas(alas, t)
    kSeg = segitiga.Keliling(s2, s2, s3)
    return kSeg*t+(2*lSeg)

def PrismaSegitiga():
    while True:
        Clear()
        print(24*'=')
        print('==' + 2*' ' + 'Prisma Segitiga' + 3*' ' + '==')
        print(24*'=')
        print('[1] Volume')
        print('[2] Luas')
        print('[98] Kembali')
        print(24*'=')
        pilih = int(input('Masukan pilihan = '))
        
        if pilih == 1:
            while True:
                Clear()
                print('Volume Prisma Segitiga :\n')
                alasSeg = int(input('Masukan alas segitiga   = '))
                tinggiSeg = int(input('Masukan tinggi segitiga = '))
                tinggiPris = int(input('Masukan tinggi prisma   = '))
                print(24*'=')
                volume = Volume(alasSeg, tinggiSeg, tinggiPris)
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
                print('Luas Prisma Segitiga :\n')
                sisi1 = int(input('Masukan sisi 1 segitiga = '))
                sisi2 = int(input('Masukan sisi 2 segitiga = '))
                sisi3 = int(input('Masukan sisi 3 segitiga = '))
                alasSeg = int(input('Masukan alas segitiga   = '))
                tinggiPris = int(input('Masukan tinggi prisma   = '))
                print(24*'=')
                luas = Luas(sisi1, sisi2, sisi3, alasSeg, tinggiPris)
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
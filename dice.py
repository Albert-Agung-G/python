import random
credit = 0
angka_dadu = random.randint(1,6)
while True:
    Tebakan = int(input('tebak angka 1 sampai 6:'))
    if angka_dadu == Tebakan:
        credit += 1
        print ('anda benar')
    else:
        print ('anda salah')
        credit -= 1
    coba = input(print ('mau mencoba lagi?:'))
    if coba == 'y':
        continue
    else:
        print (credit)
        break
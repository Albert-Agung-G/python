import random
angka = random.randint(1,20)
tebakan = 0
try:
    while True:
        Tebakan = int(input('tebak angka dari 1 sampai 20:'))
        tebakan += 1
        if tebakan == 5:
            print('terlalu banyak mencoba')
            break
        elif angka > Tebakan:
            print('angka terlalu kecil')
        elif angka < Tebakan:
            print('angka terlalu besar')
        else:
            print('angka benar')
            break
except:
    print('angka benar')
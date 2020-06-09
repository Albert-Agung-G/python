def age_calculator(tahun_lahir,tahun_sekarang):
    print(f'anda berumur {tahun_sekarang-tahun_lahir} tahun')
while True:
    tahun_lahir = int(input('berapa tahun lahir anda?:'))
    tahun_sekarang = int(input('sekarang tahun brp?:'))
    print (age_calculator(tahun_lahir,tahun_sekarang))
    ulang = input('apakah kamu mau ulang?:')
    if ulang == 'y':
        continue
    else:
        break
def nilai (dictionary):
    for key, val in dictionary.items():
        print(f'hasil {key} {val}')

Nilai = {}

while True:
    nama = input('nama:')
    angka = int(input ('nilai:'))
    if angka >= 90:
        grade  = 'A'
    elif angka > 80:
        grade = 'B'
    elif angka > 70:
        grade = 'C'
    else:
        grade = 'F'
    Nilai[nama] = angka
    another = input('add another?:')
    if another == 'y':
        continue
    else:
        break
nilai(Nilai)
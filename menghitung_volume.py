def segitiga(alas,tinggi):
    print(1/2*alas*tinggi)
def lingkaran(radius):
    print(3.14*radius*radius)
def ling(radius):
    return 3.14*radius*radius
def tabung(lingkaran,tinggi_tabung):
    print(lingkaran*tinggi_tabung)
def bola (radius):
    print(4/3*3.14*jari*jari*jari)
while True:
    hitung = input("mau hitung apa?:")
    if hitung == "segitiga":
        alas = int(input('masukan alas segitiga:'))
        tinggi = int(input('masukan tinggi segitiga:'))
        print (segitiga(alas,tinggi))
        ulang = input('apakah ada yang mau di hitung lagi?:')
        if ulang == 'y':
            continue
        else:
            break
    elif hitung == "lingkaran":
        radius = int (input('masukan radius lingkaran:'))
        print (lingkaran(radius))
        ulang = input('apakah ada yang mau di hitung lagi?:')
        if ulang == 'y':
            continue
        else:
            break
    elif hitung == "bola":
        jari = int(input('brp jari jari bola?:'))
        print (bola(jari))
        ulang = input('apakah ada yang mau di hitung lagi?:')
        if ulang == 'y':
            continue
        else:
            break
    else:
        tinggi_tabung = int(input('masukan tinggi tabung:'))
        radius = int(input('brp jari jari bola?:'))
        print (tabung(ling(radius),tinggi_tabung))
        ulang = input('apakah ada yang mau di hitung lagi?:')
        if ulang == 'y':
            continue
        else:
            break
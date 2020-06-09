operasi = input("operasi dalam? : ")
angka1 = int(input("angka dalam meter : "))
angka2 = int(input("angka2 dalam meter : "))
if operasi == '+':
    hasil= angka1 + angka2
elif operasi == '-':
    hasil= angka1 - angka2
elif operasi == '*' :
    hasil= angka1 * angka2
else:
    hasil= angka1 / angka2
print (hasil)
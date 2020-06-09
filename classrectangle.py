class segitiga:

    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas(self):
        return f'{self.alas * self.tinggi}'
segi3 = segitiga(2,2)
print (segi3.luas())

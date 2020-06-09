class Flower:
    def __init__(self, flower_name, flower_petals, flower_price):
        self.flower_name = flower_name
        self.flower_petals = flower_petals
        self.flower_price = flower_price
    
    def update_name(self, new_name):
        self.flower_name = new_name

    def update_petals(self, new_petals):
        self.flower_petals = new_petals

    def update_price(self, new_price):
        self.flower_price = new_price

    def return_name(self):
        return self.flower_name

    def return_petals(self):
        return self.flower_petals

    def return_price(self):
        return self.flower_price

    def data_bunga(self):
        print (f'bunga {self.flower_name} berkelopak {self.flower_petals} harga {self.flower_price}')

kembang = Flower('melati', 6, 12.0)
kembang.data_bunga()
kembang.update_name('kembang')
kembang.update_petals(7)
kembang.update_price(20.5)
kembang.data_bunga()
print(kembang.return_name())
melati = Flower('melati', 6, 12.0)
sepatu = Flower('sepatu', 8, 15.5)
class Pants:
    def __init__(self,color,waist_size,length,price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price 

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return self.waist_size

    def change_price(self,new_price):
        self.price = new_price 

    def discount(self, percentage):
        return self.price * (1 - percentage)


pant1 = Pants('red', 35, 36, 15.33)
print(str(pant1))
print(len(pant1))
class Product:
    def __init__(self, name, price,type):
        self.name = name
        self.price = price
        self.type = type

    def __str__(self):
        return "{0}-{1}-{2}".format(self.name, self.price, self.type)
class Shop:
    def __init__(self, listOfProducts):
        self.dictOfProducts = {}

    def calc_shop_price(self):
        price = 0
        print(self.milkProducts)
        for k, v in self.milkProducts:
            price += v

prod = Product("Milk", 1.86, "Milky")
print(prod)
sevenEleven = Shop()

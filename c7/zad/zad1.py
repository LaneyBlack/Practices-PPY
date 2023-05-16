class Product:
    def __init__(self, name, price, producer, date, type):
        self.name = name
        self.date = date
        self.price = price
        self.producer = producer
        self.type = type

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.name, self.price, self.date, self.type)


class Shop:
    def __init__(self, name, dictOfProducts):
        self.name = name
        self.dictOfProducts = dictOfProducts

    def calc_shop_price(self):
        price = 0
        for k in self.dictOfProducts.keys():
            price += k.price * self.dictOfProducts[k]
        return price

    def getStock(self):
        return {k.name: self.dictOfProducts[k] for k in self.dictOfProducts.keys()}


prod = Product("Milk", 1.86, "Milka", "22.02", "Drink")
print(prod)
prodDict = {
    prod: 10,
    Product("Water", 4.30, "Borjomi", "27.02", "Drink"): 12,
    Product("Chicken Meat", 12.4, "WMK", "04.03", "Meat"): 16,
    Product("Cucumber", 4.3, "CareForEco", "10.03", "Vegetable"): 14
}
sevenEleven = Shop("Seven Eleven", prodDict)
print(sevenEleven.getStock())
print({str(k):sevenEleven.dictOfProducts[k] for k in sevenEleven.dictOfProducts.keys()})
print("Seven eleven all stock price: " + str(sevenEleven.calc_shop_price()))
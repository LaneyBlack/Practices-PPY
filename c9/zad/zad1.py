class Product:
    def __init__(self, name, price, producer, date, type):
        self.name = name
        self.date = date
        self.price = price
        self.producer = producer
        self.type = type

    def __str__(self):
        return "{0},{1},{2},{3},{4}".format(self.name, self.price, self.producer, self.date, self.type)


def readDb(path):
    result = []
    file = open(path,mode="r", encoding="UTF-8")
    for line in file:
        values = line.strip().split(',')
        result.append(Product(*values))
    return result


def writeDb(path, products):
    with open(path, mode="w", encoding="UTF-8") as file:
        for product in products:
            file.write(str(product)+"\n")


products = readDb("prod.txt")

for prod in products:
    print(prod)

products.append(Product("Banana",2.09,"Spain","12.02","Fruit"))

writeDb("prod.txt",products)

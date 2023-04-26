def getProducts(where=None, orderBy=None):
    products = [
        {"Name": "Milk", "Producer": "Milka", "Date": "22.02", "Type": "Drink"},
        {"Name": "Water", "Producer": "Borjomi", "Date": "27.02", "Type": "Drink"},
        {"Name": "Chicken Meat", "Producer": "WMK", "Date": "04.03", "Type": "Meat"},
        {"Name": "Cucumber", "Producer": "CareForEco", "Date": "10.03", "Type": "Vegetable"},
    ]
    if where != None:
        products = filter(where, products)
    if orderBy != None:
        products.sort(key=orderBy)
    return products


print("SELECT * FROM products")
print(*getProducts(), sep="\n")
print("SELECT * FROM products WHERE Producer=Milka")
print(*getProducts(where=lambda a: a["Producer"] == "Milka"), sep="\n")
print("SELECT * FROM products ORDER BY Name")
print(*getProducts(orderBy=lambda a: a["Name"]), sep="\n")
print("SELECT * FROM products WHERE Type=Drink ORDER BY Producer")
print(*getProducts(orderBy=(lambda a: a["Name"]), where=(lambda a: a["Type"]=="Drink")), sep="\n")

# Napisz skrypt, który utworzy 5 list
shops = ["Zabka", "CareFor", "Biedronka", "Lidl", "Auchan"]
products = [
    {"Name": "Milk", "Producer": "Milka", "Date": "22.02", "Type": "Drink"},
    {"Name": "Water", "Producer": "Borjomi", "Date": "27.02", "Type": "Drink"},
    {"Name": "Chicken Meat", "Producer": "WMK", "Date": "04.03", "Type": "Meat"},
    {"Name": "Cucumber", "Producer": "CareForEco", "Date": "10.03", "Type": "Vegetable"},
]
prices = [2.93, 1.99, 15.01, 3.99]
clients = ["Jarek", "Ania", "Polya", "Piotr", "Eugene"]
boughtProducts = [""]

# Prints
print("---=---(1)---=---")
print([(shops[x], products[y]["Name"]) for x in range(len(shops))
       if x % 2 == 1
       for y in range(len(products))
       if y % 2 == 0 or y % 3 == 0])
print("---=---(2)---=---")
print({clients[i]: [products[j]["Name"] for j in range(len(products)) if i == 0 or j % i == 0]
       for i in range(len(clients))})
print("---=---(3)---=---")
# print({products[i]["Name"]: prices[len(products) - 1 - i] for i in range(len(products))})
print({products[i]["Name"]: prices[-i - 1] for i in range(len(products))})  # if lengths are same

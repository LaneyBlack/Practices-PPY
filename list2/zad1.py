# Ex1 - 4pkt
def if_lower_print(a, b, symbol):
    if (a < b):
        print(symbol, end="\t")
    else:
        print(" ", end="\t")


a, b, c = [int(x) for x in input("Please provide 3 whole numbers: ").split()]
for i in range(max(a, b, c)):
    if_lower_print(i, a, "*")
    if_lower_print(i, b, "#")
    if_lower_print(i, c, "$")
    print()
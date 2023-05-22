# Ex1 - 4pkt
def iflower_print(a, b, symbol):
    if (a < b):
        print(symbol, end="\t")
    else:
        print(" ", end="\t")


a, b, c = [int(x) for x in input("Please provide 3 whole numbers: ").split()]
for i in range(max(a, b, c)):
    iflower_print(i, a, "*")
    iflower_print(i, b, "#")
    iflower_print(i, c, "$")
    print()
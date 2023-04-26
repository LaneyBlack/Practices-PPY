"""
    Lab04 - instrukcje warunkowe (if's)
"""
print("Simple logic instructions")
print("1---")
if 1<2:
    print("true1")
if True:
    print("true2")
if "napis":
    print("true3")
if 1:
    print("true4")
if None:
    print("true5")
print("2---")
x = True
y = False
if x and y:
    print("true6")
if x or y:
    print("true7")
print("Complicated logic instructions")
print("1---")
a = -1
if a<0:
    print("1")
    if a != 20:
        print("Good"*3)
print("2---")
inp = int(input("Podaj dowolną liczbę całkowitą: "))
if  inp<0:
    print("Czerwony")
elif inp>0:
    print("Zielony")
else:
    print("Biały")

if 10<inp<100: # inp<10 and inp>100
    print("[10-100]")
else:
    print("Zły zakres")
#Ex9 - 3pkt
numbers = []
for i in range(3):
    numbers.append(int(input("Please input number {}: ".format(i+1))))
if min(numbers)<=0:
    print("Bad request! All values must be > 0")
isPythagoras = False
for a in numbers:
    if a**2 == sum([num**2 for num in numbers if num!=a]):
        isPythagoras = True
        break

if isPythagoras:
    print("This IS a Pythagoras Three!")
else:
    print("This IS NOT a Pythagoras Three!")
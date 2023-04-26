import math


def getPrimeNumbers(upto=100):
    numbers = {i:True for i in range(upto+1)}
    for num in range(2, int(math.ceil(math.sqrt(upto)))):
        if numbers[num]:
            for k in range(num * num, upto + 1, num): # get all elements divisible by num
                numbers[k] = False
    return [num for num in numbers if numbers[num]==True]


print(getPrimeNumbers())
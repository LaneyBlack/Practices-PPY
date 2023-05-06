import math


def checkForPerfectNumber(*nums):
    result = dict()
    for num in nums:
        if num not in result.keys():
            summary = 0
            for i in range(1, int(num / 2 + 1)):
                if num % i == 0:
                    summary += i
            if num == summary:
                result[num] = True
            else:
                result[num] = False
    return result


def getCatalanNumbers(upto, even=None):
    result = []
    prevNumber = 1
    for i in range(upto):
        catNum = 0
        if i == 0 or i == 1:
            catNum = 1
        else:
            catNum = ((4 * i + 2) / (i + 2)) * prevNumber
        prevNumber = catNum
        if (catNum > upto):
            break
        if even == None:
            result.append(catNum)
        elif even and catNum % 2 == 0:
            result.append(catNum)
        elif not even and catNum % 2 == 1:
            result.append(catNum)
    return result


def getPrimeNumbers(upto=100):
    numbers = {i: True for i in range(upto + 1)}
    for num in range(2, int(math.ceil(math.sqrt(upto)))):
        if numbers[num]:
            for k in range(num * num, upto + 1, num):  # get all elements divisible by num
                numbers[k] = False
    return [num for num in numbers if numbers[num] == True]

def printNumbersOnCondition(n, condition, reverse=False):
    result = []
    count, num = 0, 0
    while count < n:
        if condition(num):
            result.append(num)
            count += 1
        num += 1
    result.sort(reverse=reverse)
    print(*result, sep=", ")
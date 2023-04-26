def printNumbers(n, condition, reverse=False):
    result = []
    count, num = 0, 0
    while count < n:
        if condition(num):
            result.append(num)
            count += 1
        num += 1
    result.sort(reverse=reverse)
    print(*result, sep=", ")


printNumbers(20, lambda a: (a % 2 == 0 and a % 3 != 0))
printNumbers(10, lambda a: (a % 2 == 0 and a % 3 != 0), reverse=True)
def checkNum(*nums):
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


print(checkNum(4, 5, 6, 28, 10, 11, 8128))

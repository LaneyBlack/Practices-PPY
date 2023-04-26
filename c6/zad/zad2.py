def getCatalanNumbers(upto, even=None):
    result = []
    prevNumber=1
    for i in range(upto):
        catNum = 0
        if i == 0 or i == 1:
            catNum = 1
        else:
            catNum = ((4 * i + 2) / (i + 2)) * prevNumber
        prevNumber=catNum
        if(catNum>upto):
            break
        if even==None:
            result.append(catNum)
        elif even and catNum%2==0:
            result.append(catNum)
        elif not even and catNum%2==1:
            result.append(catNum)
    return result

print(*getCatalanNumbers(40, even=False))
print(*getCatalanNumbers(100, even=True))
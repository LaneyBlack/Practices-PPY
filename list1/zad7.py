# Ex7 - 4pkt
k = int(input("Please input a k number: "))
decision = int(input("Please choose (1)list, (2)dictionary: "))
if (decision == 1):
    print([num for num in range(20, 80) if num % k == 0])
else:
    print({k:[num for num in range(20, 80) if num % k == 0]})
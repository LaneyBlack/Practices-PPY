# Ex8 - 4pkt
start = int(input("Please input range start: "))
end = int(input("Please input range end: "))
k =  [int(x) for x in input("Please enter K's divided by space: ").split()]
print({k[i]: [num for num in range(start, end) if num % k[i] == 0] for i in range(len(k))})

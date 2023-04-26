# List declaration
print("-=-Declaration-=-")
list1 = []
print(list1)
list1 = [1, 2, 3, "PJATK", 12, 40, 10, 7, 8, 20]
print(list1)
list2: list[int] = [3, 8, 2]
print(list2)
list3 = list("lalaland")
print(list3)
# Indexing
print("-=-Indexing-=-")
print(list1[0])
print(list1[1:4])
print(list2[1:])
print(list1[::2]) # from 0 to end every second element
print(list1[:-2:2])
print(list1[1:-1:2])
print(list1[::-1]) # print from end to start
# List modification
print("-=-Modification-=-")
list1.append('o')
print(list1)
list1.append([1, 2, 4])
print(list1)
list1.insert(1,4) # place, value
print(list1)
list1.pop()
print(list1)
list1.pop(4)
print(list1)
list1.remove('o')
print(list1)
list12 = list1 + list2
print(list12)
list2 *= 3
print(list2)
list2.sort(reverse=True)
print(list2)
listA = list1 # this is reference
print(list1)
print(listA)
list1.pop()
list1.pop()
print(list1)
print(listA)
print('----------------------------------------------------------------------------')
# Tuple
tuple1 = 1,
print(tuple1)
tuple1 = (1,4,8)
print(tuple1)

tuple2 = 1, 3.14, "PJATK", [1,2], 1
print(tuple2)
print(tuple("Hello"))
# Indexing of tuples
print(tuple2[0])
print(tuple2[:2])
print(tuple2[::-1])
print(tuple2.count(1)) # how many 1's is in a Tuple
print(tuple2.index(1)) # first index of 1 in a Tuple
print('----------------------------------------------------------------------------')
# Set
set1 = {}
print(set1)
set1 = {1, 2, 1, 10, 8, 23, 13, 19}
print(set1)
set1.pop()
print('----------------------------------------------------------------------------')
# Dictionary
dict1 = {1:1, 2:3, 4:5}
print(dict1)
print('----------------------------------------------------------------------------')
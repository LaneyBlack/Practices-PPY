# Input
w1 = input(" Please type first word: ").lower()
w2 = input(" Please type second word: ").lower()
# Rozwiązanie korzystające z właściwości ASCII
for x in range(97, 123):
    # a - 97, 101 - e, 105 - i, 111 - o, 117 - u, 121 - y
    if (x in (97, 101, 105, 111, 117, 121)):
        w1 = w1.replace(chr(x), '7')
    else:
        w2 = w2.replace(chr(x), '6')

# # Rozwiązanie używając listy
# cons = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
# vowels = ['a','e','u','y','i','o']
# for v in vowels:
#     w1 = w1.replace(v,'7')
# print(w1.upper())
# for c in cons:
#     w2 = w2.replace(c, '6')

# Output
print("First word - " + w1.upper())
print("Second word - " + w2.upper())
print("Concat = " + w1.upper() + w2.upper())

"""
    Caesar cipher
"""
while (True):
    choice = int(input("Please choose what to do (1 - cipher, 2 - decipher, 3 - exit): "))
    if choice == 1:
        key = int(input("Please type key of the conversion: "))
        text = input("Please input text to cipher: ").lower()
        cipher = [(chr((ord(l) + key - 97) % 26 + 97)) for l in text if 'a' <= l <= 'z']
        for l in cipher:
            print(l, end="")
        print()
    elif choice == 2:
        key = int(input("Please type key of the conversion: "))
        text = input("Please input text to decipher: ")
        decipher = [(chr((ord(l) - key - 97) % 26 + 97)) for l in text if 'a' <= l <= 'z']
        for l in decipher:
            print(l, end="")
        print()
    else:
        break


# decipher = [char for char in text]
# for i in range(0, len(decipher)):
#     if 'a' <= decipher[i] <= 'z':
#         decipher[i] = chr((ord(decipher[i]) - key) % 26 + 97)
#     if 'A' <= decipher[i] <= 'Z':
#         decipher[i] = chr((ord(decipher[i]) - key) % 26 + 65)

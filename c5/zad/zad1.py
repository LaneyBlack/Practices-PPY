"""
    Caesar cipher
"""
while (True):
    choice = int(input("Please choose what to do (1 - cipher, 2 - decipher, 3 - exit): "))
    key = int(input("Please type key of the conversion: "))
    if choice==1:
        text = input("Please input text to cipher: ")
        cipher = [chr((ord(l) + key) % 26 + 97) for l in text if 'a'<=l<='z']
        print("".join(cipher))
    elif choice==2:
        text = input("Please input text to cipher: ")
        decipher = [chr((ord(l) - key) % 26 + 97) for l in text]
        print("".join(decipher))
    else:
        break
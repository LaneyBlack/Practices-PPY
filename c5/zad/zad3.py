# Napisz skrypt do generowania 10 haseł z trzech list:
import random

bigLetters = [chr(i) for i in range(65, 91)]
smallLetters = [chr(i) for i in range(97, 123)]
numLetters = [chr(i) for i in range(48, 58)]
passwords = []
choice = int(input("Please choose password difficulty (1 - easy, 2 - medium, 3 - hard): "))
password = []
type = 0
for i in range(10):
    password = []
    if choice == 1 or choice == 2: type = random.randrange(1, 4)
    secondChoice = 0
    if choice == 2:
        secondChoice = random.randrange(1, 4)
    for j in range(10):
        if choice == 3:
            type = random.randrange(1, 4)
        elif choice == 2:
            if secondChoice == 1:
                type = random.randrange(1, 3)
            elif secondChoice == 3:
                type = random.randrange(2, 4)
            else:
                while type == 2:
                    type = random.randrange(1, 4)

        if type == 1:
            x = random.randrange(0, len(smallLetters))
            while not (x % 2 == 0 or x % 5 == 0):
                x = random.randrange(0, len(smallLetters))
            password += smallLetters[x]
        elif type == 2:
            x = random.randrange(0, len(bigLetters))
            while not (x % 6 == 0):
                x = random.randrange(0, len(bigLetters))
            password += bigLetters[x]
        elif type == 3:
            x = random.randrange(0, len(numLetters))
            while not (x % 2 == 0):
                x = random.randrange(0, len(numLetters))
            password += numLetters[x]
    passwords.append(password)
it = iter(passwords)
for i in range(10):
    print(next(it))

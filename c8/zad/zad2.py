import random

choice = input("Please select a random (1) or increasing(2) list of 20 integers: ")
if choice == "1":
    print([random.randrange(0,20) for i in range(20)])
elif choice == "2":
    print([i for i in range(20)])
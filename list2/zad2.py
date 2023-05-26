# Ex2(Calculator) - 6pkt
from list2.Calculator import Calculator

calc = Calculator()
print("Welcome to calculator (exit to stop):")
while True:
    inp = input("Action: ").strip().split()
    if inp[0] == "exit":
        break
    if inp[0] == "help":
        calc.print_help()
        continue
    if len(inp) != 3:
        print("Wrong input!")
        print("User command 'help' to see the correct input format")
        continue
    print(calc.action(int(inp[0]), inp[1], int(inp[2])))

act = input("Do you want to print history(y/n)? ").strip()
if act == "y":
    calc.print_history()
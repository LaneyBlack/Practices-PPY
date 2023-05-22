class Calculator:
    def __init__(self):
        self.history = []

    def action(self, a, act, b):
        result = 0
        if act == "+":
            result = a + b
        elif act == "-":
            result = a - b
        elif act == "*":
            result = a * b
        elif act == "/":
            result = a / b
        elif act == "//":
            result = a // b
        elif act == "%":
            result = a % b
        elif act == "/^":
            result = a ** (1 / b)
        elif act == "^":
            result = a ** b
        else:
            print("Wrong action")
            return
        self.history.append(result)
        return result

    def print_history(self):
        print(*[x for x in self.history],sep=", ")
    def print_help(self):
        print("Supported actions: +, -, *, /, // (divide without remainder), %, /^ (sqrt), ^ (power)")
        print("Input format (separated only with spaces!) is: number1 action number2")
        print("For example: 1 % 3")

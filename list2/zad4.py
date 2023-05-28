# import random
from datetime import datetime


class Token:
    token_length = 100
    splitter = ","

    @staticmethod
    def create_token(user, date, secret):
        data = ""
        data += user.name + Token.splitter
        data += user.surname + Token.splitter
        data += user.email + Token.splitter
        data += date.strftime("%m-%d-%y %H:%M:%S") + Token.splitter
        result = ""
        secret_index = 0
        for i in range(len(data)):
            secret_index %= len(secret)
            # ---This code with random---
            # if i < len(data):
            #     character_code = ord(data[i]) + secret[secret_index]
            # if data ended flood token with random data
            # else:
            #     character_code = random.randint(0, 126) + secret[secret_index]
            character_code = ord(data[i]) + secret[secret_index]
            character_code = character_code % 126
            result += chr(character_code)
            secret_index += 1
        return result

    @staticmethod
    def translate(token, secret):
        result = ""
        secret_index = 0
        # for i in range(Token.token_length):
        for i in range(len(token)):
            secret_index %= len(secret)
            character_code = ord(token[i])
            if character_code - secret[secret_index] < 0:
                character_code += 126
            character_code -= secret[secret_index]
            result += chr(character_code)
            secret_index += 1
        return result

    @staticmethod
    def print_token(token):
        print("Token:")
        for c in token:
            print(c, end="")
        print()


class User:
    secret = [2, 3, 5, 2, 1, 4, 5, 6]

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email


def main():
    user_input = input(
        "Please provide user data to make a token(name, surname, e-mail, expire date (%m-%d-%y %H:%M:%S)): ") \
        .strip().split(",")
    user = User(user_input[0], user_input[1], user_input[2])
    token = Token.create_token(user, datetime.strptime(user_input[3].strip(), "%m-%d-%y %H:%M:%S"), user.secret)
    Token.print_token(token)
    while True:
        user_input = input("Do you want to exit (type 'exit') or login (type 'login'): ").strip()
        if user_input == "login":
            user_input = input("Please provide your token: ")
            data = Token.translate(user_input.strip(), user.secret)
            values = data.split(Token.splitter)
            exp_date = datetime.strptime(values[3].strip(), "%m-%d-%y %H:%M:%S")
            if exp_date > datetime.now():
                print("User login success!")
                print("Data: ", values[0], values[1], values[2])
                user_input = input("Do you want to check expire date(y/n)? ").strip()
                if user_input == "y":
                    print("Expire date is " + values[3])
            else:
                print("User login problem!")
                print("Token has expired")
        else:
            break


if __name__ == "__main__":
    main()

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
            character_code-=secret[secret_index]
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


# Change this to test the algorythm
token_date_expire = "05-26-23 14:43:00"


def main():
    user = User("Jan", "Kowalski", "kowalski@gmail.com")
    token = Token.create_token(user, datetime.strptime(token_date_expire, "%m-%d-%y %H:%M:%S"), user.secret)
    Token.print_token(token)
    while True:
        user_input = input("Do you want to exit (type 'exit') or login (type 'login'): ").strip()
        if user_input == "login":
            data = Token.translate(token, user.secret)
            values = data.split(Token.splitter)
            exp_date = datetime.strptime(values[3], "%m-%d-%y %H:%M:%S")
            if exp_date > datetime.now():
                print("User login success!")
                print("Data: ", values[0], values[1], values[2])
            else:
                print("User login problem!")
                print("Token has expired")
        else:
            break


if __name__ == "__main__":
    main()

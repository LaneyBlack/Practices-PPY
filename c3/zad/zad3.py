letters = input("Write 10 capital letters (separated with \", \"): ").split(", ")
numbers = input("Write 10 numbers. From 1 to 10 (separated with \", \"): ").split(", ")
dic = {letters[i]: numbers[i] for i in range(len(letters))}
# dic = dict.fromkeys(numbers, letters)
print(dic)

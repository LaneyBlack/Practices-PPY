"""
 Lalaland
"""
# Print
print("Hello Python!!!")
# Text formatting (Python 2.7)
print ("My name is %s. I am %d years old." %("Mark",25))
# Text formatting (Python 3.x)
print ("My name is {0}. I am {1} years old." .format("Mark", 25))
print ("My name is {1}. I am {0} years old." .format("Mark", 25))
# Input
x = input("What's your name?\n")
print('Hello ' + x)
# Lists and variables
print("Lists:")
print(1, 'Hello', '23', sep=' - ')
x = [1, 'Hello' , '2', [1, '3']]
print(x)
print(type(x))

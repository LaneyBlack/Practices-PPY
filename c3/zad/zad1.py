name = input("Please write your name: ")
birthDate = input("Please write your brith date: ")
email = input("Please write your email: ")
phone = input("Please write your phone number: ")
list = [name, birthDate, email, phone]
tuple = (name, birthDate, email, phone)
dict = {
    "Name" : name,
    "Birth Date" : birthDate,
    "Email" : email,
    "Phone Number" : phone
}
print("List: {}".format(list))
print("Tuple: {}".format(tuple))
print("Dictionary: {}".format(dict))
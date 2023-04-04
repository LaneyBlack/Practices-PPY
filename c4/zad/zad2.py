inNumSys = int(input("Please choose a number system you type in (2, 8, 10, 16): "))
number = int(input("Please type in a number to convert: "), inNumSys)
outNumSys = int(input("Please choose a number system to convert into (2, 8, 10, 16): "))
output = str(number)
if (outNumSys == 2):
    output = str(bin(number))
elif (outNumSys == 8):
    output = str(oct(number))
elif (outNumSys == 16):
    output = str(hex(number))
print("Result = {0} | ({1}->{2})".format(output, inNumSys, outNumSys))

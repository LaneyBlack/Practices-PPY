"""
    Lab09 - file read
"""
# Option 1
file1 = open("czarny_kot.txt", mode="r", encoding="utf-8")
text = file1.read()
# print(text)
file1.close()

print(file1.closed)

# Option 2
file2 = open("czarny_kot.txt", mode="r", encoding="utf-8")
print(file2.readline())
file2.close()

# Option 3
file3 = open("czarny_kot.txt", mode="r", encoding="utf-8")
# for line in file3:
#     print(line, end=" ")
file3.close()

# Option 4
with open("czarny_kot.txt", mode="r", encoding="utf-8") as file4:
    print(file4.readline())
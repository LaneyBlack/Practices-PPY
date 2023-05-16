"""
    Lab09 - File Write
"""

file1 = open("new_file.txt", mode="w", encoding="utf-8")
file1.write("wooooooooooooooooow")
file1.close()

file2 = open("new_file.txt", mode="w", encoding="utf-8")
f = file2.write("Example text")
file2.close()
print(f)

file3 = open("new_file.txt", mode="a", encoding="utf-8")
file3.write("\nSecond line\n")
file3.close()

with open("new_file.txt", mode="r", encoding="utf-8") as file4:
    print(file4.read())

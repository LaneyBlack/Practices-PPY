"""
    Lab09 - system commands
"""

import os

print(os.listdir("C:/Users/Public/Documents"))

path = os.path.join(os.path.expanduser("~"), "test_")
print(path)

# os.mkdir(path,0o777)
print(os.listdir(os.path.expanduser("~")))

path2 = os.path.join(os.path.expanduser("~"), "test_")
os.rename(path,path2)

(catalog, file) = os.path.split("C:/Users/Public/Documents/desktop.ini")
print(catalog)
print(file)

(catalog, type) = os.path.splitext(file)
print(catalog)
print(type)

os.rmdir(path2)
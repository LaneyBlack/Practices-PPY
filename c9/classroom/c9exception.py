"""
    Lab09 - Exceptions
"""


def get(sec, ind):
    return sec[ind]


files = ["czarny_kot.txt", "new_file.txt"]
ind = 2

try:
    print(get(files, ind))
except IndexError:
    print("Error occurred")

try:
    print(get(files, ind))
except IndexError as e:
    print("Error occurred:", e)
else:
    print("Got file name")

try:
    f = get(files, ind)
    print(f)
    file = open(f)
except (IndexError, FileNotFoundError) as e:
    print("Error occurred:", e)
else:
    print(file.readline())
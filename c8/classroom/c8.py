"""
    Lab08 - modules
"""

# import module
import datetime

t = datetime.time(10, 48, 59)
# print(t)
# print(str(t.hour) + "-" + str(t.minute))
# print(datetime.datetime.now())

# functions
import math

def countCircleSpan(r):
    return math.pi * r ** 2

def countCirclePerimeter(r):
    return math.pi * r * 2

# random
import random
# from random import *
random.seed()
print(random.randint(1,15))
print(random.randint(1,25))

l = list(range(1,10))
print(*l)
print(random.choice(l))
random.shuffle(l)
print(l)
print(random.random())
print(random.uniform(10,20))
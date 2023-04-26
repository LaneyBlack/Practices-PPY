# functions
import math
import sys


def countCircleSpan(r):
    return math.pi * r ** 2


def countCirclePerimeter(r):
    return math.pi * r * 2


def main():
    print(sys.argv)
    print(countCircleSpan(int(sys.argv[1])))

if __name__ == "__main__":
    main()

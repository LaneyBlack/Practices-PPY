"""
    Lab08 - Own modules
"""

from c8 import countCircleSpan
import c8

print(c8.t)
print(countCircleSpan(3))
print(c8.countCirclePerimeter(3))

# Package
import my_package.circle_functions as f
print(f.countCirclePerimeter(5))
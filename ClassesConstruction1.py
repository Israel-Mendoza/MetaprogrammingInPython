from math import pi
from typing import Union


class Circle:
    def __init__(self, radius: Union[int, float]) -> None:
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


# Circle is a symbol in this module
print("Circle" in globals())
# True

# Circle is an instance of type
print(type(Circle))
# <class 'type'>
print(isinstance(Circle, type))
# True

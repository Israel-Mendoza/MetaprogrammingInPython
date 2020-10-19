"""Introducing the __new__ method"""

# When instantiating an instance of a class, Python calls the __new__ method
# on the class and passes the class as the first parameter:
# my_obj = MyClass.__new__(MyClass)
# If this method is not defined by the class, it will take it from the
# parent class, as expected. In this case, it will be from "object":

from typing import Union


class Point:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        print(f"__init__ was called - self: {self}")
        self.x = x
        self.y = y


# __new__ creates the instance and returns it.
# Then __init__ is called passing the recently created instance
# returned by the __new__ method as the first argument
p1 = Point(10, 20)
# __init__ was called - self: <__main__.Point object at 0x27C57B43FD0>

# Only __new__ is called
p2 = Point.__new__(Point)
# Only __new__ is called
p3 = object.__new__(Point)

print(type(p1))  # <class '__main__.Point'>
print(type(p2))  # <class '__main__.Point'>
print(type(p3))  # <class '__main__.Point'>


"""Creating instances using object.__new__()"""


# Notice how __init__ is not called!
p1 = object.__new__(Point, 10, 20)
# (No output from __init__)

# Confirming that __init__ was not called and the namespace is empty
print(p1.__dict__)
# {}

# Calling __init__ ourselves:
p1.__init__(10, 10)
# __init__ was called - self: <__main__.Point object at 0x27C57B428B0>


# Confirming that __init__ was called and the namespace is not empty
print(p1.__dict__)
# {'x': 10, 'y': 10}

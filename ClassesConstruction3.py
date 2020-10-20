"""Creating a class creator by inheriting from type"""


from typing import Type


class CustomType(type):
    """Metaclass  which allows customization of class creation"""

    def __new__(cls: Type, name: str, bases: tuple, class_dict: dict) -> "CustomType":
        print("Creating a CustomeType type!")
        print(f"Class name: {class_name}")
        print(f"Class namespace: {class_dict}")
        class_dict["say_hello"] = lambda self: f"{self} says 'Hello, World!'"
        instance = super().__new__(cls, name, bases, class_dict)
        print(f"CustomType type created at address {hex(id(instance)).upper()}")
        # instance.say_hello = lambda self: f"{self} says 'Hello, World!'"
        return instance


"""Using the CustomType metaclass to create classes"""

# Preparing the arguments
class_name = "Person"
class_body = """
def __init__(self, name):
    print("__init__ called!")
    self.name = name

def __str__(self):
    return f"Person called {self.name}"
"""
class_bases = tuple()
exec(class_body, globals(), class_namespace := {})

# Using our CustomType class to create another class
Person = CustomType(class_name, class_bases, class_namespace)

# Instrospecting our new type
print(type(Person))  # <class '__main__.CustomType'>
print(isinstance(Person, CustomType))  # True
print(isinstance(Person, type))  # True
print(Person.__dict__)
# {'__init__': <function __init__ at 0x1AD75CE9F70>,
# '__str__': <function __str__ at 0x1AD75FF1550>,
# '__module__': '__main__',
# '__dict__': <attribute '__dict__' of 'Person' objects>,
# '__weakref__': <attribute '__weakref__' of 'Person' objects>,
# '__doc__': None,
# 'say_hello': <function CustomType.__new__.<locals>.<lambda> at 0x1AD75FF65E0>} <<--!!!

"""Creating instances of our custom type class"""

p1 = Person("Israel")
# __init__ called!
print(p1.say_hello())
# Person called Israel says 'Hello, World!'

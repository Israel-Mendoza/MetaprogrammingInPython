"""Implementing class decorator that will also decorate properties, and class and static methods"""


from functools import wraps
from typing import Callable, Type


# Simple logger function to decorate functions
def function_logger(fn: Callable) -> Callable:
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f"\nFunction called: {fn.__qualname__}({args}, {kwargs})")
        print(f"Returned value: {result}\n")
        return result

    return inner


# Class decorator that will decorate callables, properties, class and static
# methods in the decorated class using the function_logger decorator.
def logger_to_class_callables(cls: Type) -> Type:
    for attr_name, attr_value in vars(cls).items():
        if callable(attr_value):
            print(f"Decorating {cls.__name__}.{attr_name} with function_logger")
            setattr(cls, attr_name, function_logger(attr_value))
        elif isinstance(attr_value, staticmethod):
            print(f"Decorating {cls.__name__}.{attr_name} with function_logger")
            temp = staticmethod(function_logger(attr_value.__func__))
            setattr(cls, attr_name, temp)
        elif isinstance(attr_value, classmethod):
            print(f"Decorating {cls.__name__}.{attr_name} with function_logger")
            temp = classmethod(function_logger(attr_value.__func__))
            setattr(cls, attr_name, temp)
        elif isinstance(attr_value, property):
            name = cls.__name__
            if attr_value.fget:
                print(f"Decorating {name}.{attr_name} getter with function_logger")
                attr_value = attr_value.getter(function_logger(attr_value.fget))
            if attr_value.fset:
                print(f"Decorating {name}.{attr_name} setter with function_logger")
                attr_value = attr_value.setter(function_logger(attr_value.fset))
            if attr_value.fdel:
                print(f"Decorating {name}.{attr_name} deleter with function_logger")
                attr_value = attr_value.deleter(function_logger(attr_value.fdel))
            setattr(cls, attr_name, attr_value)
    return cls


@logger_to_class_callables
class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def instance_method(self):
        print(f"{self} instance says hello!")

    @staticmethod
    def static_method():
        print(f"Hello from the static method")

    @classmethod
    def class_method(cls):
        print(f"{cls.__name__} says hello!")


# Output:
# Decorating Person.__init__ with function_logger
# Decorating Person.name getter with function_logger
# Decorating Person.name setter with function_logger
# Decorating Person.instance_method with function_logger
# Decorating Person.static_method with function_logger
# Decorating Person.class_method with function_logger


p1 = Person("Israel")
# Function called: Person.__init__((<__main__.Person object at 0x0000020A099B6FA0>, 'Israel', 28), {})
# Returned value: None

p1.instance_method()
# <__main__.Person object at 0x000002ACC8206FA0> instance says hello!
# Function called: Person.instance_method((<__main__.Person object at 0x000002ACC8206FA0>,), {})
# Returned value: None

p1.name
# Function called: Person.name((<__main__.Person object at 0x1E5A4686FA0>,), {})
# Returned value: Israel

p1.name = "Mike"
# Function called: Person.name((<__main__.Person object at 0x1E5A4686FA0>, 'Mike'), {})
# Returned value: None

Person.static_method()
# Hello from the static method
# Function called: Person.static_method((), {})
# Returned value: None

Person.class_method()
# Person says hello!
# Function called: Person.class_method((<class '__main__.Person'>,), {})
# Returned value: None

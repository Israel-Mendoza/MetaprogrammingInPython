"""Using a class as a decorator"""

from typing import Any, Callable
from types import MethodType


class Logger:
    def __init__(self, a_func: Callable[..., Any]) -> None:
        self.func = a_func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f"Calling {self.func.__name__}")
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance:
            return MethodType(self, instance)
        return self


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    @Logger
    def say_hi(self):
        return f"{self.name} says 'Hello World!'"

    @classmethod
    @Logger
    def cls_method(cls):
        print(f"{cls.__name__} says hello!")

    @staticmethod
    @Logger
    def static_method():
        print("A static method says hello!")


p = Person("Israel")


try:
    print(p.say_hi())
    print(Person.say_hi())
except TypeError as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: say_hi() missing 1 required positional argument: 'self'

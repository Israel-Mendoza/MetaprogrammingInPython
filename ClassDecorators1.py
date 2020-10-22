"""Using simple class decorators"""


# Creating a couple of class decorators


from typing import Callable, Type


def savings(cls):
    cls.account_type = "savings"
    return cls


def checking(cls):
    cls.account_type = "checking"
    return cls


# Decorating classes with these class decorators


class Account:
    pass


@savings
class BankSavings1(Account):
    pass


@savings
class BankSavings2(Account):
    pass


@checking
class BankChecking1(Account):
    pass


@checking
class BankChecking2(Account):
    pass


# "account_type" was injected by the decorators

print(vars(BankSavings1))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}
print(vars(BankSavings2))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}
print(vars(BankChecking1))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}
print(vars(BankChecking2))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}


"""Recreating the same as above, but using a parameterized decorator"""

# Creating a parameterized class decorator


def account_type(acc_type: str) -> Callable[[Type], Type]:
    """Decorator factory"""

    def class_decorator(cls: Type):
        """A class decorator"""
        cls.account_type = acc_type
        return cls

    return class_decorator


# Decorating classes with the parameterized class decorators


@account_type("savings")
class BankSavings1(Account):
    pass


@account_type("savings")
class BankSavings2(Account):
    pass


@account_type("checking")
class BankChecking1(Account):
    pass


@account_type("checking")
class BankChecking2(Account):
    pass


print(vars(BankSavings1))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}
print(vars(BankSavings2))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'savings'}
print(vars(BankChecking1))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}
print(vars(BankChecking2))
# {'__module__': '__main__', '__doc__': None, 'account_type': 'checking'}


"""Using class decorator to add a function to the decorated class"""


def adding_greeting(cls):
    cls.say_hello = lambda self: f"{self} says hello!"
    return cls


@adding_greeting
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


print(vars(Person))
# {'__module__': '__main__',
# '__init__': <function Person.__init__ at 0x00000224374C9700>,
# '__str__': <function Person.__str__ at 0x00000224374C9790>,
# '__dict__': <attribute '__dict__' of 'Person' objects>,
# '__weakref__': <attribute '__weakref__' of 'Person' objects>,
# '__doc__': None,
# 'say_hello': <function adding_greeting.<locals>.<lambda> at 0x224374C9670>}

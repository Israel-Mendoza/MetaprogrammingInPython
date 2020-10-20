class Squared(int):
    """A class that represents an int"""

    def __new__(cls, x: int) -> "Squared":
        # super() == int
        # int.__new__ requires an expression to be converted to an int.
        # int.__init__ doesn't take arguments. The instance creation is
        # delegated to the __new__ method.
        # Similar as writing: new_instance = int(x ** 2)
        new_instance = super().__new__(cls, x ** 2)
        return new_instance


my_num = Squared(4)
print(my_num)
# 16
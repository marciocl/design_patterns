class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    @staticmethod
    def sum_(num1: int, num2: int) -> float:
        return num1 + num2

    @staticmethod
    def multiply(num1: int, num2: int) -> float:
        return num1 * num2

    @staticmethod
    def divide(num1: int, num2: int) -> float:
        return num1 / num2

    @staticmethod
    def sub(num1: int, num2: int) -> float:
        return num1 - num2


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

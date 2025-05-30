#!/usr/bin/pyhton3
"""Module identifies if an instance is of the class"""


def is_same_class(obj, a_class):
    """
    Will print True is from specified class.
    Otherwise prints False.
    """
    return type(obj) is a_class

    class MyClass:
        pass

    class SubClass(MyClass):

        a = MyClass()
        b = MyClass()

    print(isinstance(a, MyClass))  # Should print True
    print(isinstance(b, SubClass)) # Should print True

#!/usr/bin/python3
"""Module that identifies inherited instances"""


def inherits_from(obj, a_class):
    """
    Prints True is object was inherited from specified class,
    otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

    class MyClass:
        pass

    class SubClass(MyClass):

        a = MyClass()
        b = SubClass()

        print(isinstance(a, MyClass))
        print(isinstance(b, SubClass))

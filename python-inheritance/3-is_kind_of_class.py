#!/usr/bin/python3
"""Module determines instances are from inherited class or not"""


def is_kind_of_class(obj, a_class):
    """
    Prints True if object is intance of the class or inherited from a class
    """
    return isinstance(obj, a_class)

    class MyClass:
        pass

    class SubClass(MyClass):

        a = MyClass()
        b = SubClass()

        print(isinstance(a, MyClass))
        print(type(b, SubClass))

#!/usr/bin/python3
"""Module raises exceptions within the class BaseGeometry"""


class BaseGeometry:
    """Defines class BaseGeometry and instance methods"""

    def integer(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

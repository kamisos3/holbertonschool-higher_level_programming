#!/usr/bin/python3
"""Module raises an exception within the class BaseGeometry"""


class BaseGeometry:
    """Class with method that raises Exception"""
    def area(self):
        raise Exception("area() is not implemented")

#!/usr/bin/python3
"""Module defines square"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """Initializes square with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates area of the square and returns it"""
        return self.__size ** 2

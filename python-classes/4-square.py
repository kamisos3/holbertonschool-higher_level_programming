#!/usr/bin/python3
"""Module to define square"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """Initialize square with size"""
        self.size = size   # Uses setter to validate input

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size validated"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate squares area and returns it"""
        return self.__size ** 2

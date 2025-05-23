#!/usr/bin/python3
"""Module defines square"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """Initializes square with size"""
        self.size = size   # Validates input with setter

    @property
    def size(self):
        """Retrieves squares size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets square size validated"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates square area and returns it"""
        return self.__size ** 2

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

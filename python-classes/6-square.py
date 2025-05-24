#!/usr/bin/python3
"""Module defines square"""


class Square:
    """Represents square with size ans position attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes new square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get squares size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get squares position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of square"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print squere with # in position"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

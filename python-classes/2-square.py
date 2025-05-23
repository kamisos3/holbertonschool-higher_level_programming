#!/usr/bin/python3
"""Module to define square"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """Initialize square with given size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

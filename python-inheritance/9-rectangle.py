#!/usr/bin/python3
"""Module inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines rectangle class"""

    def __init__(self, width, height):
        """Initialize rectangle with width and height, validated"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"

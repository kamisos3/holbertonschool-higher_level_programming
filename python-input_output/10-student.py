#!/usr/bin/python3
"""Module defines Student class"""


class Student:
    """Defines the student"""

    def __init__(self, first_name, last_name, age):
        """Calls attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

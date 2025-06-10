#!/usr/bin/python3
"""Module defines Student class with instances"""


class Student:
    """Defines Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # Calls themselves with self() to print desired attributes

    def to_json(self):
        """This will retrieve dictionary version of Student class"""
        return self.__dict__

#!/usr/bin/python3
"""Module reads a text ands prints it"""


def read_file(filename=""):
    """Attribute that prints files content"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

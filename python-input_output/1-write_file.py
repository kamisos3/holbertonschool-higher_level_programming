#!/usr/bin/python3
"""Module writes a string to a text file and returns # of characters"""


def write_file(filename="", text=""):
    """This will write the line into file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

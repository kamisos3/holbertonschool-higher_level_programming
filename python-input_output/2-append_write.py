#!/usr/bin/python3
"""
Module appends a string to the end of the file
and returns # of characters added
"""


def append_write(filename="", text=""):
    """Appends string to the file to count characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

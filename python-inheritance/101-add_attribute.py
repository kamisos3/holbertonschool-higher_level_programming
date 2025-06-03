#!/usr/bin/python3
"""Module aads a new attribute to object if possible"""


def add_attribute(obj, name, value):
    """Defines add_attribute to call main"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

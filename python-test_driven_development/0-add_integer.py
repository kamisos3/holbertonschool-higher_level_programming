#!/usr/bin/python3
"""
    This module is a function too add two integers
"""


def add_integer(a, b=98):
"""Add two integers and return result as integer."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

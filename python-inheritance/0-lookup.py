#!/usr/bin/python3
"""Module defined returns a list of methods/attributes"""


def lookup(obj):
    """
    This looks for instances from object to return list
    of attributes
    """
    return dir(obj)

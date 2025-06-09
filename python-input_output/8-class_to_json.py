#!/usr/bin/python3
"""
    Module returns dictionary description with is data structure
    to serialize an object.
"""


def class_to_json(obj):
    """Prints the dictionary version of the object"""
    return obj.__dict__

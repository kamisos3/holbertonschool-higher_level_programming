#!/usr/bin/python3
"""Module defines MyInt class that inherits from int"""


class MyInt(int):
    """Class MyInt is defined here"""
    def __eq__(self, other):  # __eq__ checks == and overrides to print !=
        return super().__ne__(other)

    def __ne__(self, other):  # __ne__ checks != and overrides to print ==
        return super().__eq__(other)

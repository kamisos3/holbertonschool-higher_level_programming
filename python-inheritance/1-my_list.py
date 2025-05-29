#!/usr/bin/python3
"""Method that defines a class that inherits"""


class MyList(list):
    """This class inherits from list"""

    def print_sorted(self):
        """Prints the list sorted ascending"""
        print(sorted(self))

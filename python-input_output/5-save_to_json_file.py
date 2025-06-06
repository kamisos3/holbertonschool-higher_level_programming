#!/usr/bin/python3
"""Module writes an object to text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Writes to text file"""
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(my_obj, file)

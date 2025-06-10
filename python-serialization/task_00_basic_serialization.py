#!/usr/bin/python3
"""Module serializes data"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a dictionary to save as JSON"""
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_desirialize(filename):
    with open(filename, 'r') as file:
        return json.load(file)

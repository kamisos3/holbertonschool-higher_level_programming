#!/usr/bin/python3
"""Module returns JSON format of a string"""
import json

def to_json_string(my_obj):
    """Turns a string into JSON format"""
    return json.dumps(my_obj)

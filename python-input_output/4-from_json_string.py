#!/usr/bin/python3
"""Module returns an object like a JSON string"""
import json


def from_json_string(my_str):
    """Reurns Python data structure as JSON"""
    return json.loads(my_str)

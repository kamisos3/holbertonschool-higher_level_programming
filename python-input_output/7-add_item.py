#!/usr/bin/python3
"""Module adds script with arguments to list"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
    if not isinstance(items, list):

        items = []
except Exception:

    items = []
# Add arguments to the list

items.extend(sys.argv[1:])
# Saves list to file

save_to_json_file(items, filename)

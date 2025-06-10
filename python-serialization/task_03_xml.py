#!/usr/bin/python3
"""Module serializes and deserializes with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)

            child.text = str(value)

        tree = ET.ELementTree(root)
        tree.write(filename)

        return True
    except Exception:
        return False

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}

    except (FileNotFoundError, ET.ParseError):
        return None

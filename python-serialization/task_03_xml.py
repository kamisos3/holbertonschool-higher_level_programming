#!/usr/bin/python3
"""Module serializes and deserializes with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize Python dictionary to XML"""
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename)
        return True
    except Exception:
        print(f"Serialization error: {e}")
        return False

def deserialize_from_xml(filename):
    """Deserialize from XML to Python dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result   # Python dictionary

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except ET.ParseError as e:
        print(f"XML parse error: {e}")
        return None

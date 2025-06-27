#!/usr/bin/python3
"""Module serializes data from CSV to JSON"""
import csv
import json
import sys
import os

def convert_csv_to_json(csv_filename, json_filename="data.json"):
    """Converts CSV data and reads it"""
    try:
        with open (csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data =[row for row in reader]

    except FileNotFoundError as e:
        print(f"[ERROR] CSV file not found: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"[ERROR] Failed to read CSV file not found: {e}", file=sys.stderr)
        return False

    """Writes CSV data into JSON"""
    try:
        with open(json_filename, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True

    except Exception as e:
        print(f"[ERROR] Failed to write JSON file: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./csv_to_json.py <csv_filename> [json_filename]")
        sys.exit(1)

    csv_file = sys.argv[1]
    json_file = sys.argv[2] if len(sys.argv) > 2 else "data.json"

    if convert_csv_to_json(csv_file, json_file):
        print(f"Succesfully converted {csv_file} to {json_file}")
    else:
        print("Conversion failed")
        sys.exit(1)


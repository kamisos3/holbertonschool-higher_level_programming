#!/usr/bin/python3
"""Module serializes data"""
import pickle
import os

class CustomObject:
    """Defnes class for CustomObject"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"[OK] Serialized to {os.path.abspath(filename)}")
            return True
        except Exception as e:
            print(f"[ERROR] serialize(): {e}")
            return False

    @classmethod
    def deserialize(cls, filename):
        try:
            print(f"[INFO] Attempting to read {os.path.abspath(filename)}")
            with open(filename, 'rb') as file:
                    obj = pickle.load(file)
            print("[OK] Deserialized succesfully")
            return obj
        except Exception as e:
            print(f"[ERROR] deserialize(): {e}")
            return None

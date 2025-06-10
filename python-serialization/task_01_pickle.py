#!/usr/bin/python3
"""Module serializes data"""
import pickle


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
        except as e:
            print(f"Serialization error: {e}")

        @classmethod
        def deserialize(cls, filename):
            try:
                with open(filename, 'rb') as file:
                    return picke.load(file)
            except (FileNotFoundError, picke.PickeError):
                return None

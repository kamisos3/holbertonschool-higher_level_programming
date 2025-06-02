#!/usr/bin/python3
"""Module defines abstrac class"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Defines Animal class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Defines Dog class"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Defines Cat class"""
    def sound(self):
        return "Meow"

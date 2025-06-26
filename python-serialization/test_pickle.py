#!//usr/bin/python3
import pytest
import os
import pickle
from task_01_pickle import CustomObject

def test_display_output(capsys):
    """Tests display output"""
    obj = CustomObject(name="Alice", age=30, is_student=False)
    obj.display()
    captured = capsys.readouterr()
    assert captured.out == "Name: Alice\nAge: 30\nIs Student: False\n"

def test_serialization_roundtrip(tmp_path):
    obj = CustomObject(name="Bob", age=25, is_student=True)
    file_path = tmp_path / "test.pkl"

    obj.serialize(str(file_path))
    assert os.path.exists(file_path)

    new_obj = CustomObject.deserialize(str(file_path))

    assert new_obj.name == "Bob"
    assert new_obj.age == 25
    assert new_obj.is_student is True

def test_error_handling():
    assert CustomObject.deserialize("non_existent.pkl") is None

    obj = CustomObject(name="Test", age=0, is_student=False)
    assert obj.serialize("")

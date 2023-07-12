#!/usr/bin/python3
"""Defines unittests for state.py."""
import unittest
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test State Class"""

    def tear_down(self):
        """Delete the JSON file after testing """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(State, 'name'))

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(issubclass(type(State()), BaseModel))

    def test_no_args_instantiates(self):
        """Test type"""
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        """Test save in objects dict"""
        self.assertIn(State(), storage.all().values())

    def test_id_is_public_str(self):
        """Test type of attributes inherited"""
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        """Test type of attributes inherited"""
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test type of attributes inherited"""
        self.assertEqual(datetime, type(State().updated_at))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Defines unittests for user.py."""
import unittest
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test User Class"""

    def tear_down(self):
        """Delete the JSON file after testing """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(type(User()), BaseModel))

    def test_no_args_instantiates(self):
        """Test type"""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """Test save in objects dict"""
        self.assertIn(User(), storage.all().values())

    def test_id_is_public_str(self):
        """Test type of attributes inherited"""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Test type of attributes inherited"""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test type of attributes inherited"""
        self.assertEqual(datetime, type(User().updated_at))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Defines unittests for city.py."""
import unittest
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def tear_down(self):
        """Delete the JSON file after testing """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(type(Amenity()), BaseModel))

    def test_no_args_instantiates(self):
        """Test type"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """Test save in objects dict"""
        self.assertIn(Amenity(), storage.all().values())

    def test_id_is_public_str(self):
        """Test type of attributes inherited"""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        """Test type of attributes inherited"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test type of attributes inherited"""
        self.assertEqual(datetime, type(Amenity().updated_at))


if __name__ == '__main__':
    unittest.main()

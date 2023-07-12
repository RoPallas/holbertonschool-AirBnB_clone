#!/usr/bin/python3
"""Defines unittests for place.py."""
import unittest
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test Place class"""

    def tear_down(self):
        """Delete the JSON file after testing """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(issubclass(type(Place()), BaseModel))

    def test_no_args_instantiates(self):
        """Test type"""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """Test save in objects dict"""
        self.assertIn(Place(), storage.all().values())

    def test_id_is_public_str(self):
        """Test type of attributes inherited"""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """Test type of attributes inherited"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test type of attributes inherited"""
        self.assertEqual(datetime, type(Place().updated_at))


if __name__ == '__main__':
    unittest.main()

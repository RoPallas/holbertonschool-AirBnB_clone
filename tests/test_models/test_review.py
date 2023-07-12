#!/usr/bin/python3
"""Defines unittests for review.py."""
import unittest
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review class"""

    def tear_down(self):
        """Delete the JSON file after testing """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_attributes(self):
        """Test class attributes"""
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(issubclass(type(Review()), BaseModel))

    def test_no_args_instantiates(self):
        """Test type"""
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """Test save in objects dict"""
        self.assertIn(Review(), storage.all().values())

    def test_id_is_public_str(self):
        """Test type of attributes inherited"""
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        """Test type of attributes inherited"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test type of attributes inherited"""
        self.assertEqual(datetime, type(Review().updated_at))


if __name__ == '__main__':
    unittest.main()

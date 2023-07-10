#!/usr/bin/python3
"""Defines unittests for city.py."""
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity


class TestState(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_inheritance(self):
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(type(Amenity()), BaseModel))

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

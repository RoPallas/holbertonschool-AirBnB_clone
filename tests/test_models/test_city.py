#!/usr/bin/python3
"""Defines unittests for city.py."""
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.city import City


class TestState(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertTrue(hasattr(City, 'name'))

    def test_inheritance(self):
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(type(City()), BaseModel))

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

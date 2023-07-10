#!/usr/bin/python3
"""Defines unittests for review.py."""
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.review import Review


class TestState(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_inheritance(self):
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(issubclass(type(Review()), BaseModel))

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

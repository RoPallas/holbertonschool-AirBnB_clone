#!/usr/bin/python3
"""Defines unittests for user.py."""
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_inheritance(self):
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(type(User()), BaseModel))

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

#!/usr/bin/python3
"""Defines unittests for state.py."""
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(State, 'name'))

    def test_inheritance(self):
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(issubclass(type(State()), BaseModel))

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

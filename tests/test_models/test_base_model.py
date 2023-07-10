#!/usr/bin/python3
"""Defines unittests for base_model.py."""
import unittest
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_init_no_arguments(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIn(obj, storage.all().values())

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_str(self):
        obj = BaseModel()
        str_output = str(obj)
        self.assertIsInstance(str_output, str)
        self.assertIn(obj.__class__.__name__, str_output)
        self.assertIn(obj.id, str_output)
        self.assertIn(str(obj.__dict__), str_output)

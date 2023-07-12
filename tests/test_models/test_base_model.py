#!/usr/bin/python3
"""Unittests for BaseModel class"""
import unittest
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""

    def tear_down(self):
        """Delete the JSON file after testing """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init_no_arguments(self):
        """Test for initilice with no args"""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIn(obj, storage.all().values())

    def test_init_with_arguments(self):
        """Test for initilice with kwargs"""
        attr_dict = {}
        attr_dict["id"] = "New id"
        attr_dict["created_at"] = datetime.now().isoformat()
        attr_dict["updated_at"] = datetime.now().isoformat()
        obj = BaseModel(**attr_dict)
        storage.new(obj)
        key = f"BaseModel.{obj.id}"

        objects = storage.all()
        self.assertIn(key, objects)
        self.assertEqual(obj, objects[key])

    def test_save(self):
        """Test for save method, verify that change updated at attr"""
        obj = BaseModel()
        updated_at_1 = obj.updated_at
        obj.save()
        updated_at_2 = obj.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_to_dict(self):
        """Test for to dict method, verify correct data into dict"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_str(self):
        """Test for str method, verify correct format and data"""
        obj = BaseModel()
        str_output = str(obj)
        self.assertIsInstance(str_output, str)
        self.assertIn(obj.__class__.__name__, str_output)
        self.assertIn(obj.id, str_output)
        self.assertIn(str(obj.__dict__), str_output)


if __name__ == '__main__':
    unittest.main()

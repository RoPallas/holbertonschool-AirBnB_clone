#!/usr/bin/python3
"""Unittests for FileStorage class"""
import unittest
import os
import json
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageClass(unittest.TestCase):
    """Test for FilageStore Class"""

    def tear_down(self):
        """Delete the JSON file after testing """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test all method, verify that it generates a dictionary"""
        objects = storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """Test new method, verify that news objects
        are saved in the dictionary"""
        obj = BaseModel()
        key = f"BaseModel.{obj.id}"

        attr_dict = {}
        attr_dict["id"] = "New id"
        attr_dict["created_at"] = datetime.now().isoformat()
        attr_dict["updated_at"] = datetime.now().isoformat()
        obj_2 = BaseModel(**attr_dict)
        storage.new(obj_2)
        key_2 = f"BaseModel.{obj_2.id}"

        objects = storage.all()
        self.assertIn(key, objects)
        self.assertEqual(obj, objects[key])
        self.assertIn(key_2, objects)
        self.assertEqual(obj_2, objects[key_2])

    def test_save(self):
        """Test save method, verify that create a file and
        save the object inside"""
        obj = BaseModel()
        obj.save()
        key = f"BaseModel.{obj.id}"
        file = "file.json"
        self.assertTrue(os.path.exists(file))
        with open(file, "r") as f:
            content = json.load(f)
        self.assertIn(key, content)

    def test_reload(self):
        """Test reload method, verify that reaload an obj
        from a JSON file"""
        obj = BaseModel()
        storage.save()
        storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertTrue(key in storage.all())


if __name__ == '__main__':
    unittest.main()

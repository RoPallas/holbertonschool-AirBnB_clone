#!/usr/bin/python3
import unittest
from unittest import TestCase
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(TestCase):

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(storage), FileStorage)


    def test_new(self):
        obj = BaseModel()
        storage.new(obj)
        objects = storage.all()
        self.assertIn(obj, objects.values())


if __name__ == '__main__':
    unittest.main()

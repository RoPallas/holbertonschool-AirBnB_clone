#!/usr/bin/python3
"""Class FileStorage"""
import json
import os


class FileStorage():
    """Class FileStorage"""

    def __init__(self):
        """"""
        self.__file__path = "file.json"
        self.__objects = {}

    def all(self):
        """"""
        return self.__objects

    def new(self, obj):
        """"""
        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj

    def save(self):
        """"""
        dict_obj = {}
        for k, object in self.__objects.items():
            dict_obj[k] = object.to_dict()
        with open(self.__file__path, "w") as filename:
            json.dump(dict_obj, filename)

    def reload(self):
        """"""
        from models.base_model import BaseModel

        if os.path.exists(self.__file__path):
            with open(self.__file__path, "r") as filename:
                data = json.load(filename)
                self.__objects = {}
                for k, obj_data in data.items():
                    self.__objects[k] = BaseModel(**obj_data)

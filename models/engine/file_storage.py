#!/usr/bin/python3
"""Class FileStorage"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """Class FileStorage"""

    __file__path = "file.json"
    __objects = {}
    class_dict = {
        'BaseModel': BaseModel,
        'User': User
    }

    def all(self):
        """"""
        return self.__objects

    def new(self, obj):
        """"""
        k = obj.__class__.__name__ + "." + obj.id
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
        if os.path.exists(self.__file__path):
            with open(self.__file__path, "r") as filename:
                data = json.load(filename)
            for k, obj_data in data.items():
                class_name = k.split('.')[0] 
                self.__objects[k] = self.class_dict[class_name](**obj_data)

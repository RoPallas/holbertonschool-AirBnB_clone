#!/usr/bin/python3
"""Class FileStorage"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage():
    """Class FileStorage

    Serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attr:
        __file__path (str) - The path to the JSON file to save and load data
        __objects (dict) - Dictionary of objects saved in the JSON file
        class_dict (dict) - Dictionary of class available
    Methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """

    __file__path = "file.json"
    __objects = {}
    class_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'State': State,
        'Review': Review
    }

    def all(self):
        """Return dict of objects"""
        return self.__objects

    def new(self, obj):
        """Add a new obj to dict of objects"""
        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj

    def save(self):
        """Save the objects in a json File"""
        dict_obj = {}
        for k, object in self.__objects.items():
            dict_obj[k] = object.to_dict()
        with open(self.__file__path, "w") as filename:
            json.dump(dict_obj, filename)

    def reload(self):
        """Reload the objects from the json File, if exists"""
        if os.path.exists(self.__file__path):
            with open(self.__file__path, "r") as filename:
                data = json.load(filename)
            for k, obj_data in data.items():
                class_name = k.split('.')[0]
                self.__objects[k] = self.class_dict[class_name](**obj_data)

#!/usr/bin/python3
"""Class BaseModel"""
import uuid
from datetime import datetime


class BaseModel():
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """"""
        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """"""
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        return new_dict

    def __str__(self):
        """"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

#!/usr/bin/python3
"""Class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """"""
        if len(kwargs) > 0:
            format_date = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if k == '__class__':
                    pass
                elif k == 'created_at':
                    self.created_at = datetime.strptime(v, format_date)
                elif k == 'updated_at':
                    self.updated_at = datetime.strptime(v, format_date)
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        return new_dict

    def __str__(self):
        """"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

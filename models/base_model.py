#!/usr/bin/python3
"""Class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialice an instance of BaseModel"""
        if kwargs:
            format_date = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k in ['created_at', 'updated_at']:
                    date_value = datetime.strptime(v, format_date)
                    setattr(self, k, date_value)
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Save object"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a complete object's dict"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        return new_dict

    def __str__(self):
        """Print class name, id and dict"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

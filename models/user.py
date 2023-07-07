#!/usr/bin/python3
"""Class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User"""

    def __init__(self, *args, **kwargs):
        """Instance an User"""
        super().__init__(self, *args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
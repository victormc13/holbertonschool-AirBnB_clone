#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

"""Define the BaseModel class"""


class BaseModel:
    """
    BaseModel class that serves as the base for other classes.

    Public instance attributes:
    - id (str): Unique identifier for each instance.
    - created_at (datetime): Creation timestamp.
    - updated_at (datetime): Last update timestamp.

    Public instance methods:
    - __str__(): Returns a string representation of the instance.
    - save(): Updates the 'updated_at' attribute with the current datetime.
    - to_dict(): Converts the instance to a dictionary for serialization.
    """
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        Sets unique id, creation timestamp, and update timestamp.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: Formatted string with class name, id, and attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance to a dictionary for serialization.


        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

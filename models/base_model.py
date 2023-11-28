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
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)





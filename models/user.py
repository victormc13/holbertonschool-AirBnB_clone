#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel to represent a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

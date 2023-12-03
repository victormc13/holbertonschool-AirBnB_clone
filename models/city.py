#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits from BaseModel to represent a city. """
    state_id = ""
    name = ""

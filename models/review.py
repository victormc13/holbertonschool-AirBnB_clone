#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits from BaseModel to represent a review """
    place_id = ""
    user_id = ""
    text = ""

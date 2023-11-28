import unittest
from datetime import datetime
from base_model import BaseModel
# import models

# BaseModel = models.base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """
    def test_init(self):
        """
        Test the initialization of a BaseModel instance.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """
        Test the __str__ method of the BaseModel class.
        """
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.number = 42
        expected_dict = "'name': 'Test Model', 'number': 42,\
                        'updated_at': {my_model.updated_at},\
                        'id': '{my_model.id}',\
                        'created_at': {my_model.created_at}"
        expected_str = f"[BaseModel] ({my_model.id}) {expected_dict}"
        self.assertEqual(str(my_model), expected_str)

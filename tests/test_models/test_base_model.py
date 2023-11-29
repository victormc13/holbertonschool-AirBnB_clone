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
	str_output = str(my_model)
	self.assertIn("[BaseModel]", str_output)
	self.assertIn(f"{my_model.id})", str_output)
    
    def test_save(self):
        """
	Test the save method updates 'updated_at'.
	"""
	my_model = BaseModel()
	original_updated_at = my_model.updated_at
	my_model.save()
	self.assertNotEqual(my_model.updated_at, original_updated_at)

    def test_to_dict(self):
	"""
	Test the to_dict method for correct dictionary representation.
	"""
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
	self.assertEqual(my_model_dict['__clas__'], 'BaseModel')
	self.assertIn('id', my_model_dict)
	self.assertIn('created_at', my_model_dict)
	self.assertIn('updated_at', my_model_dict)

if __name__ = '__main__':
    unittest.main()

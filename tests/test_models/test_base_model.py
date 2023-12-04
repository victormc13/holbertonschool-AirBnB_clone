#!usr/bin/python3

"""Test cases for the BaseModel class."""

import unittest
import os
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """Set up the test environment."""
        self.file_path = "test_base_model_save.json"
        self.storage = storage
        self.storage._FileStorage__file_path = self.file_path
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after the test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

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
        self.assertIn(f"{my_model.id}", str_output)

    def test_save(self):
        """
        Test the save method updates 'updated_at'.
        """
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertNotEqual(my_model.updated_at, original_updated_at)
        obj_dict = my_model.to_dict()
        obj_dict_updated_at = obj_dict['updated_at']
        self.assertEqual(my_model.updated_at.isoformat(), obj_dict_updated_at)
        self.assertNotEqual(my_model.updated_at.utcnow(), obj_dict_updated_at)

    def test_save_persists_to_file_storage(self):
        """Test if save() persists the BaseModel instance
        to the file storage."""
        self.model.save()
        loaded_storage = storage
        loaded_storage.reload()
        all_objs = loaded_storage.all()
        key = "BaseModel.{}".format(self.model.id)
        self.assertIn(key, all_objs)
        loaded_model = all_objs[key]
        self.assertEqual(loaded_model.updated_at, self.model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method for correct dictionary representation.
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        my_model.__dict__['name'] = "Test Model"
        self.assertIn('name', my_model.__dict__)


if __name__ == '__main__':
    unittest.main()

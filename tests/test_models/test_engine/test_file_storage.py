#!/usr/bin/python3

"""Test cases for the FileStorage class."""

import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment before each test case."""
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.model = BaseModel()

    def tearDown(self):
        """Clean up the test environment after each test case."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test the 'all' method of FileStorage."""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """Test the 'new' method of FileStorage."""
        self.storage.new(self.model)
        all_objs = self.storage.all()
        key = "BaseModel.{}".format(self.model.id)
        self.assertIn(key, all_objs)

    def test_save(self):
        """Test the 'save' method of FileStorage."""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test the 'reload' method of FileStorage."""
        self.storage.new(self.model)
        self.storage.save()
        loaded_storage = FileStorage()
        with self.assertRaises(TypeError):
            loaded_storage.reload("incorrect_type_parameter")
        loaded_storage.reload()
        all_objs = loaded_storage.all()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, all_objs)

    def test_reload_docstring(self):
        """Test for reload method documentation"""
        instance = FileStorage()
        self.assertIsNotNone(instance.reload.__doc__)

    def test_reload_types(self):
        """Test the types of parameters for the 'reload' method."""
        self.storage.new(self.model)
        self.storage.save()

        loaded_storage = FileStorage()

        with self.assertRaises(TypeError):
            loaded_storage.reload("incorrect_parameter")

        loaded_storage.reload()

        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, loaded_storage.all())

    def test_reload_nonexisting_file(self):
        """Test for a non-existing file when reload the storage."""
        self.storage.new(self.model)
        self.storage.save()
        os.remove(self.file_path)
        loaded_storage = FileStorage()
        loaded_storage.reload()
        self.assertGreaterEqual(len(loaded_storage.all()), 0)


if __name__ == '__main__':
    unittest.main()

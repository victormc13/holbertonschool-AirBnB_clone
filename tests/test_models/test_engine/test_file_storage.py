import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
	"""Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment before each test case."""
        self.file_path = "test_file.json"
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
        loaded_storage.reload()
        all_objs = loaded_storage.all()
        key = "BaseModel.{}".format(self.model.id)
        self.assertIn(key, all_objs)


if __name__ == '__main__':
    unittest.main()

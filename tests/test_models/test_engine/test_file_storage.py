import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        self.storage.new(self.model)
        all_objs = self.storage.all()
        key = "BaseModel.{}".format(self.model.id)
        self.assertIn(key, all_objs)

    def test_save(self):
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        self.storage.new(self.model)
        self.storage.save()
        loaded_storage = FileStorage()
        loaded_storage.reload()
        all_objs = loaded_storage.all()
        key = "BaseModel.{}".format(self.model.id)
        self.assertIn(key, all_objs)


if __name__ == '__main__':
    unittest.main()

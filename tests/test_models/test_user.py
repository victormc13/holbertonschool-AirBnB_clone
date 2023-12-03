#!/usr/bin/pyhton3

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Class to test the User class"""

    def test_user_instance(self):
        """Tests if User is an instance of BaseModel and has the correct attributes. """
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_attribute_types(self):
        """Test the attribute types of User."""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_save(self):
        """Try User's save method."""
        user = User()
        old_created_at = user.created_at
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)

    def test_user_to_dict(self):
        """Try the to_dict method of User."""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)
        self.assertTrue('email' in user_dict)
        self.assertTrue('first_name' in user_dict)
        self.assertTrue('last_name' in user_dict)
		self.assertTrue('id' in user_dict)


if __name__ == '__main__':
    unittest.main()

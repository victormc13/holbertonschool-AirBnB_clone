#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity_instance(self):
        """Tests if amenity is an instance of Amenity and
        has the correct attributes. """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3

import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_review_instance(self):
        """Tests if review is an instance of Review class and
        has the correct attributes. """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review_attribute_types(self):
        """Test the attribute types of Review."""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.place_id, str)


if __name__ == '__main__':
    unittest.main()

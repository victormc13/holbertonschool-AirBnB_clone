#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_state_instance(self):
        """Tests if state is an instance of State class and
        has the correct attributes with an empty value"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()

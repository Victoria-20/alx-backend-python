#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests"""


import unittest
from unittest import mock
from unittest.mock import patch
import utils
from parameterized import parameterized, expand


class TestAccessNesMap(unittest.TestCase):
    """Import the TestCase class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), (1)),
        ({"a": {"b": 2}}, ("a",), ({"b": 2})),
        ({"a": {"b": 2}}, ("a", "b"), (2)),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test the utils.access_nested_map method"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()

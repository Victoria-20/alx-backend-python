#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests"""


import unittest
from parameterized import parameterized, expand


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand(
        nested_map={"a": 1}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a", "b")
    )
    def test_access_nested_map(self, nested_map, path):
        self.assertEqual(access_nested_map(nested_map, ("license", "key")) == license_key)


if __name__ == '__main__':
    unittest.main()





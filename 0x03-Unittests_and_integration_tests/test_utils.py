#!/usr/bin/env python3

"""
Unit tests for utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json, memoize


class TestGetJson(unittest.TestCase):
    """
    Test cases for get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases for memoize decorator.
    """

    class TestClass:
        """
        Test class for memoize decorator.
        """

        def a_method(self):
            """
            Test method for memoize decorator.
            """
            return 42

        @memoize
        def a_property(self):
            """
            Test property for memoize decorator.
            """
            return self.a_method()

    def test_memoize(self):
        """
        Test memoize decorator.
        """
        test_obj = self.TestClass()
        with patch.object(self.TestClass, 'a_method', return_value=42)\
                as mock_method:
            result1 = test_obj.a_property
            result2 = test_obj.a_property
            mock_method.assert_called_once()
            self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()

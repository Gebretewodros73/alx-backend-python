#!/usr/bin/env python3
"""
Generic utilities for github org client.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json, memoize


class TestGetJson(unittest.TestCase):
    """
    Test class for get_json function.
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

        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assert that the mock get was called with the correct URL
        mock_get.assert_called_once_with(test_url)
        # Assert that the result matches the expected payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test class for memoize decorator.
    """

    class TestClass:
        """
        Test class with memoized method.
        """

        def a_method(self):
            """
            Return 42.
            """
            return 42

        @memoize
        def a_property(self):
            """
            Memoized property.
            """
            return self.a_method()

    def test_memoize(self):
        """
        Test memoize decorator.
        """

        # Create an instance of the TestClass
        test_obj = self.TestClass()

        # Mock the a_method with a return value of 42
        with patch.object(self.TestClass, 'a_method', return_value=42)\
                as mock_method:
            # Call the memoized property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Assert that the mock method was called once
            mock_method.assert_called_once()

            # Ensure a_method is called only once and the results are equal
            self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()

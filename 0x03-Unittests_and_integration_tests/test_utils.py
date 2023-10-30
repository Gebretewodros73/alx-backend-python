#!/usr/bin/env python3

"""
Unit tests for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, org, expected_payload, mock_get_json):
        """
        Test org method of GithubOrgClient class.
        """
        mock_get_json.return_value = expected_payload

        github_client = GithubOrgClient(org)
        result = github_client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")
        self.assertEqual(result, expected_payload)


if __name__ == '__main__':
    unittest.main()

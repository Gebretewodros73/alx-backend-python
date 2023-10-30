#!/usr/bin/env python3
"""
GithubOrgClient module.
"""

import requests
from typing import List


class GithubOrgClient:
    """
    Class for interacting with the GitHub API.
    """

    def __init__(self, org_name: str) -> None:
        """
        Initialize the GithubOrgClient with the provided organization name.
        """
        self.org_name = org_name

    def org(self) -> dict:
        """
        Get information about the organization.
        """
        url = f"https://api.github.com/orgs/{self.org_name}"
        response = self._get_json(url)
        return response

    def public_repos(self) -> List[dict]:
        """
        Get the list of public repositories for the organization.
        """
        url = self._public_repos_url()
        response = self._get_json(url)
        return response

    def _public_repos_url(self) -> str:
        """
        Generate the URL for getting the list of public repositories.
        """
        return f"https://api.github.com/orgs/{self.org_name}/repos"

    def _get_json(self, url: str) -> dict:
        """
        Make an HTTP GET request and return the JSON response.
        """
        response = requests.get(url)
        return response.json()

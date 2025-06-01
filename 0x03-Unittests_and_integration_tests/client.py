#!/usr/bin/env python3
"""Client module for interacting with GitHub's API."""

import requests
from utils import memoize

class GithubOrgClient:
    """Client for GitHub organization."""

    def __init__(self, org_name):
        self.org_name = org_name

    @memoize
    def org(self):
        """Fetches organization information."""
        url = f"https://api.github.com/orgs/{self.org_name}"
        return requests.get(url).json()

    @property
    def _public_repos_url(self):
        """Retrieves the public repositories URL."""
        return self.org().get("repos_url")

    def public_repos(self, license=None):
        """Fetches public repositories, optionally filtered by license."""
        url = self._public_repos_url
        repos = requests.get(url).json()
        if license is None:
            return [repo["name"] for repo in repos]
        return [repo["name"] for repo in repos if repo.get("license", {}).get("key") == license]

    @staticmethod
    def has_license(repo, license_key):
        """Checks if a repository has a specific license."""
        return repo.get("license", {}).get("key") == license_key

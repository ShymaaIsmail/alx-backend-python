#!/usr/bin/env python3
"""Unit tests for GithubOrgClient."""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.requests.get')
    def test_org(self, org_name, mock_get):
        """Test org method returns expected data."""
        expected = {"login": org_name}
        mock_get.return_value.json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), expected)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property returns expected URL."""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test/repos"}
        client = GithubOrgClient("test")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test/repos")

    @patch('client.requests.get')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get):
        """Test public_repos method returns expected repository names."""
        mock_repos_url.return_value = "https://api.github.com/orgs/test/repos"
        mock_get.return_value.json.return_value = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
        ]

        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        self.assertEqual(client.public_repos(license="apache-2.0"), ["repo1"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method returns correct boolean."""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)

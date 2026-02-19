import unittest
from unittest.mock import patch, Mock
from github_api_hw4a import get_repo_commit_summary, GitHubPIError


class TestGitHubApiMocked(unittest.TestCase):

    @patch("github_api_hw4a.requests.get")
    def test_valid_user(self, mock_get):
       
        mock_repo_response = Mock()
        mock_repo_response.status_code = 200
        mock_repo_response.json.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]

    
        mock_commit_response = Mock()
        mock_commit_response.status_code = 200
        mock_commit_response.json.return_value = [{}] * 5

       
        mock_get.side_effect = [
            mock_repo_response,
            mock_commit_response,
            mock_commit_response
        ]

        result = get_repo_commit_summary("fakeuser")

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][1], 5)

    @patch("github_api_hw4a.requests.get")
    def test_invalid_user(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(GitHubPIError):
            get_repo_commit_summary("baduser")


if __name__ == "__main__":
    unittest.main()
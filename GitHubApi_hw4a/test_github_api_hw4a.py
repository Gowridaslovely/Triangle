import unittest
from github_api_hw4a import get_repo_commit_summary, GitHubPIError

class TestGitHubApi(unittest.TestCase):

    def test_valid_user(self):
        result = get_repo_commit_summary("octocat")
        self.assertTrue(len(result) > 0)

    def test_invalid_user(self):
        with self.assertRaises(GitHubPIError):
            get_repo_commit_summary("thisuserdoesnotexist123456")

if __name__ == "__main__":
    unittest.main()
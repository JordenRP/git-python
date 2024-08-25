import unittest
from unittest.mock import patch, MagicMock
from app.git_utils import init_repo, commit_changes, push_to_remote
from git import Repo

class TestGitUtils(unittest.TestCase):

    @patch('app.git_utils.Repo')
    @patch('os.makedirs')
    @patch('os.path.exists', return_value=False)
    def test_init_repo_new(self, mock_exists, mock_makedirs, mock_repo):
        repo_path = "/fake/path/to/repo"
        init_repo(repo_path)
        mock_makedirs.assert_called_once_with(repo_path)
        mock_repo.init.assert_called_once_with(repo_path)

    @patch('app.git_utils.Repo')
    @patch('os.path.exists', side_effect=lambda path: path.endswith('.git'))
    def test_init_repo_existing(self, mock_exists, mock_repo):
        repo_path = "/fake/path/to/repo"
        init_repo(repo_path)
        mock_repo.assert_called_once_with(repo_path)

    @patch.object(Repo, 'git')
    def test_commit_changes(self, mock_git):
        mock_repo = MagicMock()
        mock_repo.index.diff.return_value = True
        commit_changes(mock_repo)
        mock_repo.git.add.assert_called_once_with(A=True)
        mock_repo.index.commit.assert_called_once()

    @patch('app.git_utils.Repo.create_remote')
    @patch('app.git_utils.Repo.remotes', new_callable=MagicMock)
    def test_push_to_remote(self, mock_remotes, mock_create_remote):
        mock_repo = MagicMock()

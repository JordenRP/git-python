import unittest
from unittest.mock import patch, MagicMock
import time

from app.backup import monitor_directories

class TestBackup(unittest.TestCase):

    @patch('app.backup.init_repo')
    @patch('app.backup.commit_changes')
    @patch('app.backup.push_to_remote')
    @patch('os.path.exists', return_value=True)
    def test_monitor_directories(self, mock_exists, mock_push, mock_commit, mock_init):
        mock_repo_instance = MagicMock()
        mock_init.return_value = mock_repo_instance

        with patch('app.backup.BACKUP_DIRECTORIES', ['/test/directory']):
            try:
                monitor_directories()
            except KeyboardInterrupt:
                pass
        
        mock_init.assert_called_once()
        mock_commit.assert_called_once()
        mock_push.assert_called_once()

if __name__ == "__main__":
    unittest.main()

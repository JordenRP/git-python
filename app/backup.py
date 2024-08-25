import time
import os
from app.git_utils import init_repo, commit_changes, push_to_remote
from app.config import BACKUP_DIRECTORIES, GIT_REPO_PATH, REMOTE_REPO_URL, CHECK_INTERVAL

def monitor_directories():
    """
    Основная функция для мониторинга директорий и автоматического резервного копирования.
    """
    repo = init_repo(GIT_REPO_PATH)
    
    while True:
        print("Проверка изменений...")
        changes_detected = False

        for directory in BACKUP_DIRECTORIES:
            if not os.path.exists(directory):
                print(f"Директория {directory} не найдена.")
                continue

            repo.git.add(directory)
            changes_detected = True

        if changes_detected:
            commit_changes(repo)
            push_to_remote(repo, REMOTE_REPO_URL)
        
        print(f"Ожидание {CHECK_INTERVAL} секунд до следующей проверки...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_directories()

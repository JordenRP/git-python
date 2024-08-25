import os
from git import Repo

def init_repo(repo_path):
    """
    Инициализация Git-репозитория, если он еще не инициализирован.
    """
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)
    
    if not os.path.exists(os.path.join(repo_path, '.git')):
        repo = Repo.init(repo_path)
        print(f"Инициализирован новый репозиторий Git в {repo_path}")
    else:
        repo = Repo(repo_path)
        print(f"Используется существующий репозиторий Git в {repo_path}")
    
    return repo

def commit_changes(repo, message="Автоматическое резервное копирование"):
    """
    Добавление всех изменений и создание коммита.
    """
    repo.git.add(A=True)
    if repo.index.diff("HEAD") or repo.untracked_files:
        repo.index.commit(message)
        print(f"Изменения закоммичены с сообщением: {message}")
    else:
        print("Нет изменений для коммита.")

def push_to_remote(repo, remote_url):
    """
    Отправка изменений в удаленный репозиторий.
    """
    if 'origin' not in [remote.name for remote in repo.remotes]:
        repo.create_remote('origin', remote_url)
    
    origin = repo.remotes.origin
    origin.push()
    print(f"Изменения отправлены на удаленный репозиторий: {remote_url}")

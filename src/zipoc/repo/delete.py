import shutil
from pathlib import Path


def repository_delete():
    repo_path = Path(".zipoc")
    if not repo_path.exists():
        print("Zipoc repository hasn't been initialized!")
        return 0

    confirm = input(
        "Are you sure? Deleting a repository is irreversible and your data will be lost! (y/n) > "
    ).strip().lower()

    if confirm not in ("y", "yes"):
        print("Aborted deletion.")
        return 0

    try:
        shutil.rmtree(repo_path)  
        print("Successfully deleted zipoc repository!")
        return 0
    except Exception as e:
        print(f"Error while trying to delete zipoc repository: {e}")
        return 0

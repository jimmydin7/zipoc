from pathlib import Path
import shutil
from datetime import date

def export_commit(commit_hash):
    repo_path = Path(".zipoc")
    commits_dir = repo_path / "commits"
    src_commit_path = commits_dir / commit_hash

    if not src_commit_path.exists():
        print(f"Commit {commit_hash} not found!")
        return

    print(f"Located commit at {src_commit_path}!")

    export_name = get_export_name(commit_hash)
    exports_folder = repo_path / "exports"
    destination_folder = exports_folder / export_name


    destination_folder.mkdir(parents=True, exist_ok=True)

    shutil.copytree(src_commit_path, destination_folder, dirs_exist_ok=True)
    print(f"Exported commit to {destination_folder}!")

def get_export_name(commit_hash):
    today = date.today().strftime("%Y-%m-%d")
    return f"zipoc-{commit_hash}-{today}"
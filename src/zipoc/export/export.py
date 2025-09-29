from pathlib import Path
import shutil
from datetime import date
from zipoc.logs.logger import log

def get_export_name(commit_hash: str) -> str:
    return f"{date.today()}-{commit_hash}"

def export_commit(commit_hash):
    repo_path = Path(".zipoc")
    commits_dir = repo_path / "commits"
    src_commit_path = commits_dir / commit_hash

    if not src_commit_path.exists():
        log("error", f"Commit {commit_hash} not found!")
        return

    log("info", f"Located commit at {src_commit_path}!")

    export_name = get_export_name(commit_hash)
    exports_folder = repo_path / "exports"
    destination_folder = exports_folder / export_name


    destination_folder.mkdir(parents=True, exist_ok=True)

    shutil.copytree(src_commit_path, destination_folder, dirs_exist_ok=True)

 
    zip_path = shutil.make_archive(
        base_name=str(destination_folder), 
        format="zip",
        root_dir=str(destination_folder.parent),
        base_dir=export_name
    )

    shutil.rmtree(destination_folder)

    log("info", f"Exported commit zipped at {Path(zip_path).resolve()}!")

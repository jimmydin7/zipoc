from pathlib import Path

def export_commit(commit_hash):
    
    repo_path = Path(".zipoc")
    commits_dir = repo_path / "commits"
    specific_commit_path = commits_dir / commit_hash
    print(f"Located commit on {specific_commit_path}!")


import shutil
import json
from pathlib import Path
from datetime import datetime
from zipoc.hash.generate_hash import generate_commit_hash
from zipoc.utils.get_init_data import MetaData
import sys
import os

def copy_project_files(src_dir, dest_dir, ignore_patterns=None):
    
    if ignore_patterns is None:
        ignore_patterns = ['.git', '.zipoc', '__pycache__', '*.pyc', '.idea', 'venv', 'env', 'node_modules']
    
    
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    
    for item in src_dir.iterdir():
        
        if any(item.match(pattern) for pattern in ignore_patterns):
            continue
            
        dest_item = dest_dir / item.name
        if item.is_dir():
            copy_project_files(item, dest_item, ignore_patterns)
        else:
            shutil.copy2(item, dest_item)

def create_commit_metadata(commit_message):
    """Create metadata for the commit."""
    meta = MetaData()
    date, user_machine = meta.get_data()
    
    return {
        "commit_hash": generate_commit_hash(),
        "message": commit_message,
        "timestamp": date,
        "author": user_machine,
        "files": []  
    }

def commit_command():
    
    repo_path = Path(".zipoc")
    if not repo_path.exists():
        print("Error: Not a zipoc repository. Run 'zipoc init' first.")
        return 1
    
    
    try:
        commit_message = input("Enter commit message: ").strip()
        if not commit_message:
            print("Error: Commit message cannot be empty.")
            return 1
            
        
        commits_dir = repo_path / "commits"
        commits_dir.mkdir(exist_ok=True)
        
        
        commit_hash = generate_commit_hash()
        commit_dir = commits_dir / commit_hash
        

        metadata = create_commit_metadata(commit_message)
        
        
        (commit_dir / "files").mkdir(parents=True, exist_ok=True)
        
        
        project_root = Path(".")
        copy_project_files(project_root, commit_dir / "files")
        
        
        with open(commit_dir / "metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)
            
        print(f"Commit created: {commit_hash}")
        print(f"Message: {commit_message}")
        return 0
        
    except KeyboardInterrupt:
        print("\nCommit aborted by user.")
        return 1
    except Exception as e:
        print(f"Error creating commit: {str(e)}")
        return 1

from pathlib import Path
import json
import sys
import os

from zipoc.utils.get_init_data import MetaData


def repository_init():
    repo_path = Path(".zipoc")
    if repo_path.exists():
        print("Zipoc repository already initialized!")
        return 0

    repo_path.mkdir()

    project_name = input("Project name > ").strip().replace(" ", "-")
    project_desc = input("Project description (press enter to leave empty) > ").strip()

    user = MetaData()
    date, meta = user.get_data()

    config = {
        "project_name": project_name,
        "project_description": project_desc,
        "created_at": date,
        "user_machine": meta,
    }

    config_path = repo_path / "config.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

    print(f"Zipoc repository initialized in {repo_path.resolve()}")
    print(f"Project name: {project_name or 'N/A'}")
    print(f"Description: {project_desc or 'N/A'}")
    print(f"Created at: {date}")
    print(f"User@Machine: {meta}")
    return 0

def repository_delete():
    repo_path = Path(".zipoc")
    if repo_path.exists():
        print("Zipoc repository hasn't been initialized!")
        return 0
    os.remove(repo_path)
    
    return 0

def show_help():

    print("""
zipoc - help menu
          
zipoc init
⤷ Initialize a new zipoc repository
          
zipoc commit
⤷ Make a commit on the current repository
          
zipoc delete
⤷ Delete the current repository
          
zipoc view
⤷ View all commit & change history on a localhost web UI!
""")
    return 0

def commit_command():

    print("doggy")
    return 0


def main():
    args = sys.argv[1:]
    if not args:
        return show_help()

    cmd = args[0]

    if cmd in {"help", "-h", "--help"}:
        return show_help()
    if cmd == "commit":
        return commit_command()
    if cmd == "init" or cmd == "initialize":
        return repository_init()
    if cmd == "delete":
        return repository_delete()

    print(f"Unknown command: {cmd}\n Use 'zipoc --help' for more information.")
    return show_help()


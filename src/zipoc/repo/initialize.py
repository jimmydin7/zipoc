from pathlib import Path
import json
from zipoc.utils.get_init_data import MetaData
from zipoc.logs.logger import log

def repository_init():
    repo_path = Path(".zipoc")
    if repo_path.exists():
        log("warning", "Zipoc repository already initialized!")
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

    log("info", f"Zipoc repository initialized in {repo_path.resolve()}")
    log("info", f"Project name: {project_name or 'N/A'}")
    log("info", f"Description: {project_desc or 'N/A'}")
    log("info", f"Created at: {date}")
    log("info", f"User@Machine: {meta}")
    return 0

from flask import Flask, render_template
import logging
from pathlib import Path
import json
from zipoc.logs.logger import log as zlog

app = Flask(__name__)

def load_project_info(repo_path: Path):
    config_path = repo_path / "config.json"
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return {
                "project_name": data.get("project_name", "Unnamed Project"),
                "project_description": data.get("project_description", ""),
                "created_at": data.get("created_at", ""),
                "user_machine": data.get("user_machine", ""),
            }
        except Exception:
            pass

    return {
        "project_name": "N/A",
        "project_description": "",
        "created_at": "",
        "user_machine": "",
    }

def load_commits(repo_path: Path):
    commits_root = repo_path / "commits"
    commits = []
    if not commits_root.exists() or not commits_root.is_dir():
        return commits

    for commit_dir in sorted(commits_root.iterdir(), key=lambda p: p.stat().st_mtime, reverse=False):
        if not commit_dir.is_dir():
            continue
        meta_path = commit_dir / "metadata.json"
        meta = {}
        if meta_path.exists():
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    meta = json.load(f)
            except Exception:
                meta = {}

        commit_hash = meta.get("commit_hash") or commit_dir.name
        commits.append({
            "number": len(commits) + 1,
            "message": meta.get("message", ""),
            "timestamp": meta.get("timestamp", ""),
            "author": meta.get("author", ""),
            "hash": commit_hash, #now being stored in commits json instead of just the folder name!
            "cpath": str(commit_dir.resolve())
        })
    return commits

@app.route("/")
def home():
    repo_path = Path(".zipoc")
    project = load_project_info(repo_path) if repo_path.exists() else None
    commits = load_commits(repo_path) if repo_path.exists() else []
    total_commits = len(commits)
    return render_template('index.html', project=project, commits=commits, total_commits=total_commits, is_repo=repo_path.exists())

def run_server():

    wlog = logging.getLogger('werkzeug')
    wlog.setLevel(logging.ERROR)

    zlog("info", "Starting Zipoc viewer...\nVisit http://localhost:8080 in your browser.")
    app.run(port=8080, debug=False, use_reloader=False)
    zlog("info", "Zipoc viewer running at http://localhost:8080")

if __name__ == "__main__":
    run_server()

# Zipoc

A lightweight, local versioning tool for any project. Zipoc lets you initialize a repository, create commits of your working directory, and view them in the terminal or a simple web UI.

## Features

- Initialize a project-scoped repository in `.zipoc/`
- Create commits that snapshot your project files
- Delete the repository when you’re done
- View commits via terminal (planned) or a Flask-powered web UI


## Installation

You can install Zipoc directly from pip
( NOT RELEASED YET!)

```bash
# from the project root
python -m pip install zipoc
```


## Usage

Zipoc exposes a simple CLI via `zipoc <command>`

### Help

```bash
zipoc --help
```

### Initialize a repository

Creates a `.zipoc/` folder with a `config.json` that records project metadata.

```bash
zipoc init
```

You’ll be asked for:

- Project name
- Project description (optional)


### Make a commit

Creates a new commit under `.zipoc/commits/<hash>/` containing:

- `metadata.json` with commit hash, message, timestamp, and author
- `files/` directory with a snapshot copy of your project files (common folders like `.git`, `__pycache__`, and virtual envs are ignored)

```bash
zipoc commit
```
### View commits

Start the viewer. View commits and other data about your repository in either a localhosted web UI or your terminal

```bash
# Web UI
zipoc view --web

# Terminal UI
zipoc view --terminal
```

### Delete repository

Removes the `.zipoc/` folder and all tracked data. This is irreversible.

```bash
zipoc delete
```

Made with <3 by jim
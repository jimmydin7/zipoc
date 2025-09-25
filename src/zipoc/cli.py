import sys
from .repo import initialize as init
from .repo import delete as delete
from zipoc.utils.get_init_data import MetaData
from .utils import help_cmd as h
from .ui import app




def commit_command():

    print("doggy")
    return 0


def main():
    args = sys.argv[1:]
    if not args:
        return h.show_help()

    cmd = args[0]

    if cmd in {"help", "-h", "--help"}:
        return h.show_help()
    if cmd == "commit":
        return commit_command()
    if cmd == "init" or cmd == "initialize":
        return init.repository_init()
    if cmd == "delete":
        return delete.repository_delete()
    if cmd == "view":
        return app.run_server()

    print(f"Unknown command: {cmd}\n Use 'zipoc --help' for more information.")
    return h.show_help()


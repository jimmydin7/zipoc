import sys
from .repo import initialize as init
from .repo import delete
from .commits import commit
from .utils import help_cmd as h
from .web_ui import app as wapp
from .export import export_commit





def main():
    args = sys.argv[1:]
    if not args:
        return h.show_help()

    cmd = args[0]

    if cmd in {"help", "-h", "--help"}:
        return h.show_help()
    if cmd == "commit":
        return commit.commit_command()
    if cmd == "init" or cmd == "initialize":
        return init.repository_init()
    if cmd == "delete":
        return delete.repository_delete()

    if cmd == "view":
        if "--terminal" in args:
            print("starting terminal view!")

        elif "--web" in args:
            return wapp.run_server()
    
    if cmd == "export":
        commit_hash = sys.argv[1]
        print(f"Exporting commit ({commit_hash})")
            
            
    
    print("""Invalid arguments. Please use
zipoc view --terminal 
⤷ View commits and data on your terminal
                  
zipoc view --web
⤷ View commits and data on a localhosted web UI          
                  """)
    return 


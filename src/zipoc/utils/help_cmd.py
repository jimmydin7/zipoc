from zipoc.logs.logger import log

def show_help():

    log("info", """
zipoc - help menu
          
zipoc init
⤷ Initialize a new zipoc repository
          
zipoc commit
⤷ Make a commit on the current repository
          
zipoc delete
⤷ Delete the current repository
          
zipoc view
⤷ View all commit & change history on a localhost web UI!
|
|  --terminal  
|    ⤷ view in a terminal version
|         
|  --web  
|    ⤷ view in a localhosted web ui

        
----
Version: 0.1.0
Zipoc is open-source! Star the repository here! https://github.com/jimmydin7/zipoc
----         
""")
    return 0
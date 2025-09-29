from colorama import Fore, Style, init


init(autoreset=True)

logtypes = {
    "info": Fore.LIGHTCYAN_EX,
    "warning": Fore.LIGHTRED_EX,
    "error": Fore.RED
}

def log(logtype, msg):
    color = logtypes.get(logtype.lower(), Fore.WHITE)
    print(f"{color}[{logtype.upper()}]{Style.RESET_ALL} {msg}")

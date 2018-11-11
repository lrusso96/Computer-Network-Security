from colorama import init, Back, Fore, Style

DEBUG = Back.RESET + Fore.LIGHTMAGENTA_EX + Style.BRIGHT
ACCENT = Back.RESET + Fore.LIGHTYELLOW_EX + Style.BRIGHT
ERROR = Back.RESET + Fore.LIGHTRED_EX + Style.BRIGHT
OK = Back.RESET + Fore.GREEN + Style.BRIGHT
NORMAL = Style.RESET_ALL

def print_init():
    init()

def print_debug(*args, **kwargs):
    print( DEBUG + " ".join(map(str,args)), **kwargs)

def print_error(*args, **kwargs):
    print( ERROR + " ".join(map(str,args)), **kwargs)

def print_ok(*args, **kwargs):
    print( OK + " ".join(map(str,args)), **kwargs)

def print_normal(*args, **kwargs):
    print( NORMAL + " ".join(map(str,args)), **kwargs)

def print_accent(*args, **kwargs):
    print( ACCENT + " ".join(map(str,args)), **kwargs)

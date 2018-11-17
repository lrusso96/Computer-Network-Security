from time import time, strftime, localtime
from datetime import timedelta
from PrintUtils import *

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def log(d, elapsed=None):
    line = "="*60
    print_init()
    print_debug(line)
    print_debug(secondsToStr() + "\n")
    if d:
        for k in d:
            print_normal(k, end = " ")
            print_accent(d[k])
    if elapsed:
        print_debug("Execution time:", elapsed)
    print_debug(line)
    print_normal()
    


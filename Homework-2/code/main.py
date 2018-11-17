from Floyd import floyd_collision
from CollisionFinder import *
from LogUtils import *
import atexit
import argparse
import sys
from collections import OrderedDict

# init with header
start = time()
fields = OrderedDict()
fields["Title"] = "Collision finder on weakened SHA-1"
fields["Author"] = "Luigi Russo"
fields["Student ID"] = "1699981"
log(d = fields)

# endlog settings
def endlog():
    print()
    end = time()
    elapsed = end-start
    log(None, elapsed = secondsToStr(elapsed))

atexit.register(endlog)

#set the main parser
parser = argparse.ArgumentParser(description='SHA-1 Collision Detector')
parser.add_argument('-m', type=str, help='N=Naive Approach, L=Looping, F=Floyd', default = None)
parser.add_argument('-k', type=int, help='number of bits', default=40)
parser.add_argument('-i', type=str, help='starting index for looping algorithm', default = '0')
parser.add_argument('-n', type=int, help='number of strings to loop on', default =  5* 10**8)
parser.add_argument('--restore', help='restore previous state', action='store_true')

#create the parser
args = parser.parse_args()

#run the chosen method
method = args.m
if method == None:
    print("Method", method," not supported.")
    sys.exit(1)
try:
    if method == "F":
        floyd_collision(args.k, args.restore)
    elif method == "L":
        find_collision_looping(bits = args.k, num = args.n, start = args.i)
    elif method == "N":
        find_collision(args.k)
except ValueError:
    print("ERROR: the number of bits must be >= 4")
    sys.exit(1)

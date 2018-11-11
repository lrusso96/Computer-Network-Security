import hashlib
import string
import sys
from PrintUtils import *

def floyd_collision(bits, restore = False, debug = True):
    k = bits // 4
    if k <= 0:
        raise ValueError()

    print_init()    #colorama setup
    
    birthday_num = 2 ** (2*k)
    temp_file = "floyd.txt"
    start = "Hello world!"
    epoch_size = 10 ** 7
    step_size = birthday_num // 1000
    if bits < 50:    
        step_size = birthday_num // 200
    
    if restore:
        with open(temp_file, "r") as fin:
            cnt = int(fin.readline().strip())
            epoch = int(fin.readline().strip())
            if epoch > 0:
                epoch-=1
            dig_1 = fin.readline()[:-1]
            dig_2 = fin.readline()[:-1]
    else:
        cnt = 0
        epoch = 0
        dig_1 = hashlib.sha1(start.encode("utf-8")).hexdigest()[40-k:]
        dig_2 = hashlib.sha1(start.encode("utf-8")).hexdigest()[40-k:]
        dig_2 = hashlib.sha1(dig_2.encode("utf-8")).hexdigest()[40-k:]

    if debug:
        print_debug("starting from epoch #" +  str(epoch) + ", step #" + str(cnt))
        print_debug("actual digests:", dig_1, dig_2)
        
    print_normal("Searching for a loop: ", end = "", flush = True)
    msg = "epoch #%i  -  birthday ratio: %.1f %%" % (epoch, (100* (cnt/birthday_num)))
    while dig_1 != dig_2:
        if cnt %  epoch_size == 0:
            epoch+=1
            with open(temp_file, "w") as fout:
                print(cnt, epoch, dig_1, dig_2, sep = "\n", file = fout)
        if cnt % step_size == 0:
            msg = "epoch #%i  -  birthday ratio: %.1f %%" % (epoch, (100* (cnt/birthday_num)))
            print_accent(msg + chr(8) * len(msg), end = "", flush = True)
            
        dig_1 = hashlib.sha1(dig_1.encode("utf-8")).hexdigest()[40-k:]
        dig_2 = hashlib.sha1(dig_2.encode("utf-8")).hexdigest()[40-k:]
        dig_2 = hashlib.sha1(dig_2.encode("utf-8")).hexdigest()[40-k:]
        cnt+=1

    print_ok("DONE" + " "*len(msg)+"\n", end = "", flush = True)
    if debug:
        print_debug("Number of strings generated: ", cnt)
    print_normal("Computing the collision ", end = "", flush = True)
    dig_1 = start

    #ugly dots print...
    cnt_2 = 0
    dots = 0
    while dig_1 != dig_2:
        if cnt_2 % step_size == 0:
            if dots == 0:
                msg = ".  "
            elif dots == 1:
                msg = ".. "
            else:
                msg = "..."
                dots = -1
            dots+=1
            print_accent(msg + chr(8) * len(msg), end = "", flush = True)
        cnt_2+=1
        str_1 = dig_1
        dig_1 = hashlib.sha1(dig_1.encode("utf-8")).hexdigest()[40-k:]
        str_2 = dig_2
        dig_2 = hashlib.sha1(dig_2.encode("utf-8")).hexdigest()[40-k:]
    print_ok("DONE" + " "*len(msg))
    print()
    print_normal("Collision found:", end = " ")
    print_ok(str_1, str_2)
    print_normal("Colliding hash:", end = " ")
    print_ok(dig_1)
    
    return str_1, str_2, dig_1, cnt


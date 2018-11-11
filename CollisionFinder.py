import itertools
import hashlib
import string
import time
import os

def find_collision(bits = 48):
    k = bits // 4
    if k <= 0:
        raise ValueError()
    chars = string.printable
    d = dict()

    i = 0
    while True:
        i+=1
        print("processing... iteration #", i)
        for comb in itertools.product(chars, repeat = i):
            word = "".join(comb).encode('utf-8')
            m = hashlib.sha1()
            m.update(word)
            dig = m.hexdigest()[40-k:]
            if dig in d:
                print("found collision:", word, d[dig])
                print(dig)
                return d[dig], word, len(d)
            d[dig] = word


def _find_collision_with_set(k):
    chars = string.printable
    s = set()
    i = 0
    while True:
        i+=1
        print("processing... iteration #", i)
        for comb in itertools.product(chars, repeat = i):
            word = "".join(comb).encode('utf-8')
            m = hashlib.sha1()
            m.update(word)
            dig = m.hexdigest()[40-k:]
            if dig in s:
                print("found collision for word:", word, "and dig:", dig)
                return word, dig
            s.add(dig)
    

def find_collision_with_set(bits = 48):
    k = bits // 4
    if k <= 0:
        return
    chars = string.printable
    word, dig = _find_collision_with_set(k)
    
    i = 0
    while True:
        i+=1
        print("searching... iteration #", i)
        for comb in itertools.product(chars, repeat = i):
            word_2 = "".join(comb).encode('utf-8')
            m = hashlib.sha1()
            m.update(word_2)
            dig_2 = m.hexdigest()[40-k:]
            if dig == dig_2: # no need to check dig == dig_2
                print("found collision:", word, word_2)
                print("digest:", dig)
                return word, word_2, dig

def find_collision_looping(bits = 56, num = 5* 10**8, start = '0'):
    k = bits // 4
    if k <= 0:
        raise ValueError()

    step_size = num/1000
    hex_chars = string.hexdigits[:16]
    chars = string.printable
    for c in hex_chars[hex_chars.find(start):]:
        os.system('cls')
        dicts = {}
        for h in hex_chars:
            dicts[h] = {}
        cnt = 0
        for comb in itertools.product(chars, repeat = 5):     
            if cnt < num:
                cnt+= 1
                if cnt % step_size == 0:
                    print("processing", c, " - 1/2 (",  round(100*(cnt/num), 1), "% )", end = "\r")
        
                word = "".join(comb).encode('utf-8')
                dig = hashlib.sha1(word).hexdigest()[40-k:]
                letter = dig[1]
                if dig[0] == c:
                    short_dig = dig[2:]
                    if short_dig in dicts[letter]:
                        print("found collision:", word, dicts[letter][short_dig])
                        return dicts[letter][short_dig], word
                    dicts[letter][short_dig] = word
            
            elif cnt < 2*num:
                cnt+= 1
                if cnt % step_size == 0:
                    print("processing", c, " - 2/2 (",  round(100*(cnt/num), 1), "% )", end = "\r")
        
                word = "".join(comb).encode('utf-8')
                dig = hashlib.sha1(word).hexdigest()[40-k:]
                letter = dig[1]
                if dig[0] == c:
                    short_dig = dig[2:]
                    if short_dig in dicts[letter]:
                        print("found collision:", word, dicts[letter][short_dig])
                        return dicts[letter][short_dig], word
            else:
                break

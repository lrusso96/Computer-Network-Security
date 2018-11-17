# Homework 2

### Goal
Find a collision on a weakened SHA-1

### How to run

    python main.py

    optional arguments:
    -h, --help  show this help message and exit
    -m M        N=Naive Approach, L=Looping, F=Floyd
    -k K        number of bits
    -i I        starting index for looping algorithm
    -n N        number of strings to loop on
    --restore   restore previous state

## Examples

Floyd's algorithm:

    python main.py -m F -k 40 [--restore]

Naive algorithm:

    python main.py -m N -k 40

Modified Naive algorithm:

    python main.py -m L -k 40 [-i I] [-n N]

    


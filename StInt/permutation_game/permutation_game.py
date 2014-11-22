# Enter your code here. Read input from STDIN. Print output to STDOUT

import string

def increasing(lst):
    if len(lst) == 1:
        return True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

mem = {}

def winner(lst):
    tup = tuple(lst)
    if tup in mem:
        return mem[tup]
    else:
        if increasing(lst):
            return False
        for i in range(len(lst)):
            sublst = list(lst)
            sublst.pop(i)
            if not winner(sublst):
                mem[tup] = True
                return True
        mem[tup] = False
        return False


[t] = map(int,string.split(raw_input()))

for i in xrange(t):
    [n] = map(int,string.split(raw_input()))
    sequence = map(int,string.split(raw_input()))
    if winner(sequence):
        print "Alice"
    else:
        print "Bob"

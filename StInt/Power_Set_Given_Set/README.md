Given a string or a set. Find the power set of the given set. 
eg. Set  = {a, b, c}

Start a binary counter of set-size bits from 0 to power_set_size
If the bit is set, print that index element from the original set
000 --> {}
001 --> {c}
010 --> {b}
011 --> {b, c}
100 --> {a}
101 --> {a, c}
110 --> {a, b}

and so on and so forth

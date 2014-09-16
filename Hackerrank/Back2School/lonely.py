from collections import Counter

T = int(input())

p = map(int, raw_input().split(" "))
if len(p) == T:
    c = Counter(p)
    for i in range(len(c.keys())):
        if c.keys()[i]==1:
            print c.values()[i]
        

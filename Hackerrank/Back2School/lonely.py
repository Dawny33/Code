from collections import Counter

T = int(input())

p = map(int, raw_input().split(" "))
ans = 0
if len(p) == T:
    c = Counter(p)
    for i in range(len(c.keys())):
        if c.values()[i]==1:
            print c.keys()[i]        

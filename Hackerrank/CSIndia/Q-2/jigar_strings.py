from collections import Counter

T = int(input())

for _ in range(T):
    s = raw_input()
    c = Counter(s)
    for i in range(len(c.values())):
        if c.values()[i]!=c.values()[i-1]:
            ans = c.values()[i]
    print ans

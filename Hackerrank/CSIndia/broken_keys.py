T = int(input())

for _ in range(T):
    s = raw_input()
    s = set(s)
    if len(s):
        s1 = raw_input()
        s1 = set(s1)
        diff = s1-s
        print len(s1) - len(diff)

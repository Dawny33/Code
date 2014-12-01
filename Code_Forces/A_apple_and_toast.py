import sys

T = input()
s = [int(i) for i in sys.stdin.readline().split()]
s = sorted(s)

summ = sum(s)

if len(s)==1:
    print summ

else:
    t = sum(s)
    p = 2*t
    for i in xrange(0,T-2):
        t -= s[i]
        p += t
    print p

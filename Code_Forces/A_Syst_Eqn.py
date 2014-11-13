import sys

n,m = [int(i) for i in sys.stdin.readline().split()]

c = 0

for a in xrange(32):
    for b in xrange(32):
        if (a*a)+b-n == a+(b*b)-m==0:
            c += 1

print c

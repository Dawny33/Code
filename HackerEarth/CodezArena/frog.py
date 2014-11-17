import sys
T = input()
s = [int(i) for i in sys.stdin.readline().split()]

P = input()
while(P):
    P -= 1
    q = [int(i) for i in sys.stdin.readline().split()]
    if q[2]>q[1]:
        print -1
    else:
        print 2

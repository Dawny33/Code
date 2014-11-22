import sys
T = input()
while(T):
    T -= 1
    N,M = [int(i) for i in sys.stdin.readline().split()]
    arr = []
    while(M):
        M -= 1
        p = [int(i) for i in sys.stdin.readline().split()]
        arr = arr + p
        print arr
    q = input()
    while(q):
        q -= 1
        s = [int(i) for i in sys.stdin.readline().split()]
        if s[0] in arr and s[1] in arr:
            print "YES"
        else:
            print "NO"

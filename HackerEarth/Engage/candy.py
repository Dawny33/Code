T = int(input())

while(T):
    T -= 1
    x = map(int,raw_input().split())
    s = map(int, raw_input().split())

    sor = sorted(s)

    total = 2*s[1]
    if sum(s) <= total:
        print "YES"
    else:
        print "NO"

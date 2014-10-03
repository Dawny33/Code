T = int(input())

while(T):
    T -= 1

    n,m = map(int, raw_input().split())

    s = map(int, raw_input().split())
    if len(s)==n:
        #print m
        #print sum(s)
        if (m+sum(s)) %n ==0:
            print "Yes"
        else:
            print "No"

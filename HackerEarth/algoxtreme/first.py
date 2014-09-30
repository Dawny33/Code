T = int(input())

while(T):
    T -= 1
    n,k = map(int,raw_input().split())
    s = map(int,raw_input().split())

    if len(s)==n:
        s = sorted(s)
        #print s
        print sum(s[::-1][:k])

    

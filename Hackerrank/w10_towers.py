N = int(input())

K = int(input())

k1 = map(int,raw_input().split())

if(len(k1)<=K):
    if K==1 and k1[0]==1:
        print 2
    else:
        print k1[0]*K

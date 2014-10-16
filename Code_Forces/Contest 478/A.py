s = [int(i) for i in raw_input().split()]

if sum(s)%5==0:
    print sum(s)/5
else:
    print "-1"

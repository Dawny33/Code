T = int(input())

for _ in range(T):
    m,n = map(int,raw_input().split())
    sums = 0
    for i in range(1,m+1):
        sums += i**n
    sums = str(sums)
    if len(sums[-2:]) == 1:
        print "0" + sums[-2:]
    else:
        print sums[-2:]

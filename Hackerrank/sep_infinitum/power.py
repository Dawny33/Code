T = int(input())

while(T):
    T -= 1
    m,n = map(int,raw_input().split())
    sums = 0
    i=1
    while (i<=m):
        sums += i**n
        i += 1
        
    sums = str(sums)
    if len(sums[-2:]) == 1:
        print "0" + sums[-2:]
    else:
        print sums[-2:]




    


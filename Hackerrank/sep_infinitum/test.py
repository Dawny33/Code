T = int(input())

for _ in range(T):
    s = int(input())
    sums = 0
    count = 0
    for i in range(1,s):
        sums += (i**2)
        count += 1
        if sums>=s:
            break
    if s==1:
        print 1
    elif sums>s:
        print count-1
    else:
        print count

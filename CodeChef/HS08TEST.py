a = raw_input().split()

a[0] = int(a[0])
a[1] = float(a[1])

if a[0]<a[1]:
    if (a[0]%5 !=0) or (a[0]+0.5>a[1]):
        ans = a[1]
        print "%.2f" %ans
    else:
        ans2 = a[1] - a[0] - 0.5
        print "%.2f" %ans2
else:
    print "%.2f" %a[1]
        

from fractions import gcd

a,b,n = map(int, raw_input().split())

while(True):
    if (n>0):
        n -= gcd(a,n)
    else:
        print "1"
        break

    if (n>0):
        n -= gcd(b,n)
    else:
        print "0"
        break

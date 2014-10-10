a = [int(i) for i in raw_input().split()]
b = [int(i) for i in raw_input().split()]
c = [int(i) for i in raw_input().split()]
d = [int(i) for i in raw_input().split()]
e = [int(i) for i in raw_input().split()]

if 1 in a:
    p = a.index(1)
    print 2+ abs(3 - (p+1))

if 1 in b:
    p = b.index(1)
    print 1+ abs(3 - (p+1))

if 1 in c:
    p = c.index(1)
    print abs(3 - (p+1))

if 1 in d:
    p = d.index(1)
    print 1+ abs(3 - (p+1))

if 1 in e:
    p = e.index(1)
    print 2+ abs(3 - (p+1))



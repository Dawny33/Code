import sys

T = input()
x = y = z = 0
while(T):
    T -= 1
    s = [int(i) for i in sys.stdin.readline().split()]
    x += s[0]
    y += s[1]
    z += s[2]
if x==0 and y==0 and z==0:
    print "YES"
else:
    print "NO"

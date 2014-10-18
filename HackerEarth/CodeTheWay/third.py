import math

T = int(raw_input())

while(T):
    T -= 1
    s = raw_input()
    strr = s.split()
    a = int(strr[0])
    b = int(strr[1])
    if b == 0:
        print "1"
    else:
        a %= 10
        b %= 4
        if b==0:
            b=4
        print pow(a, b) % 10


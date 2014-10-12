import random

T = input()

if T%2==0:
    p = 8
    print str(p) + " " + str(T-p)

else:
    p = 9
    print str(p) + " " + str(T-p)

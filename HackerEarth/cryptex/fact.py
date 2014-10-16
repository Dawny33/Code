import math

T = input()

while(T):
    T -= 1
    s = input()
    f = str(math.factorial(s))
    print "%05d" %int(f[-5:])

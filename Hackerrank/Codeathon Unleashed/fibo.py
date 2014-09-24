import math

phi = (1 + math.sqrt(5)) / 2

def f(n):
    return math.floor(phi**n / math.sqrt(5) + 1/2)

T = int(input())

while(T):
    T -= 1

    s = int(input())

    if s==1:
        print 0
    else:
        sums = 0
        i = 0
        while(i!=s):
            sums += f(i)
            i += 1
        print sums%1000000007

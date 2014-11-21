import math
def is_fibo(n):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n

T = input()

while(T):
    T -= 1
    s = input()
    if is_fibo(s)==True:
        print "is fibo"
    else:
        print "not fibo"

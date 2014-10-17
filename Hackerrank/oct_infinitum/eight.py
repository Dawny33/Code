T = input()



def power(b, p):
    res = 1
    while p:
        if p & 1:
            res *= b
        b *= b
        p >>= 1

    return res

while(T):
    T -= 1
    n,a,b,m = [int(i) for i in raw_input().split()]
    summ = 0
    i = 0
    while(i<=n):
        summ += power(i,a)*power(b,i)
        i += 1

    print summ%m

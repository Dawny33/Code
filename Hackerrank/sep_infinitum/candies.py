T = int(input())

while(T):
    T -=1
    n = int(input())
    i = 1
    while True:
        s = (i*(i+1)*(2*i+1))/6
        if n<s:
            print i-1
            break
        elif n==s:
            print i
            break
        i += 1

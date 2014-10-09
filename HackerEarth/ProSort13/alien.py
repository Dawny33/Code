T = input()

def st(x):
    if x == 1:
        return 2
    if x == 2:
        return 7
    else:
        return (st(x-1) + 2*st(x-2))




while(T):
    T -= 1
    s = input()
    print st(s)%1000000007

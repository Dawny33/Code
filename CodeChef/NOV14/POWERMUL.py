import sys
T = input()

def func(d):
    if d == 1:
        return 1
    else:
        return func(d-1)*pow(d,d)


while(T):
    T -= 1
    N,M,Q = [int(i) for i in sys.stdin.readline().split()]

    while(Q):
        Q -= 1
        r = input()
        print (func(N)/(func(r)*func(N-r)))%M

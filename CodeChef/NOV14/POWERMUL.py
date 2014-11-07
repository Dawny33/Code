T = input()

def func(d):
    prod = 1
    for j in range(1,d+1):
        prod *= pow(j,j)
    return prod



while(T):
    T -= 1
    N,M,Q = [int(i) for i in raw_input().split()]

    while(Q):
        Q -= 1
        r = input()
        print (func(N)/(func(r)*func(N-r)))%M

def fun(L):
    while(len(L)>1):
        a = L[0]
        b = L[1]
        L.remove(L[1])
        L[0] = a+b+(a*b)
    return L[0]%1000000007

T = input()

s = [int(i) for i in raw_input().split()]

print fun(s)

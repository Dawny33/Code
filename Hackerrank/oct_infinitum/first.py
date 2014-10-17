import math

def fun(A):
    summ = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            summ += math.floor((A[i]+A[j])/(A[i]*A[j]))
    return summ

T = input()
while(T):
    T -= 1
    s = input()
    t = [int(i) for i in raw_input().split()]
    if len(t)==s:
        print int(fun(t))

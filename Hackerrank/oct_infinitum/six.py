def fun(A,M):
    x = len(A)
    summ = 0
    for i in range(0,x):
        if A[i]<M:
            summ += A[i]
        else:
            break
    return summ

P = input()

N = input()
r = [int(j) for j in raw_input().split()]

Q = input()
while(Q):
    Q -= 1
    s = input()

    print (fun(r,s))%P

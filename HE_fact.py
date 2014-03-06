def fact(N):
    if N==0:
        return 1
    else:
        return N*fact(N-1)

T = int(raw_input())
for i in range(0,T):
    N=int(raw_input())
    print fact(N)
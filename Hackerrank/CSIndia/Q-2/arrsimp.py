T = int(input())

def mat(A):
    if len(A) == 1:
        return A[0]
    else:
        B = []
        i = 1
        while (i < len(A)):
            B.append(A[i-1]-A[i])
            i += 1
        return mat(B)


for _ in range(T):
    s = int(input())
    t = map(int,raw_input().split())
    if len(t)==s:
        print mat(t)

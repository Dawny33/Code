T = int(input())


def is32(n):
     try:
         bitstring=bin(n)
     except (TypeError, ValueError):
         return False
         
     if len(bin(n)[2:]) <=32:
         return True
     else:
         return False


def mat(A):
    if len(A) == 1:
        return A[0]
    else:
        i = 1
        B = []
        for i in range(1,len(A)):
            B.append(A[i-1]-A[i])            
            #print B
        return mat(B)

if T<=5:
     for _ in range(T):
         s = int(input())
         t = map(int,raw_input().split())
         check = []         
         for i in t:
             check.append(is32(i))
         if False not in check:
             if len(t)==s:
                 print (mat(t)%1000000007)

T = input()

A = []
B = []
C = []
D = []
E = []

while(T):
    T -= 1
    a,b = raw_input().split()
    b = int(b)
    if a == "A":
        A.append(b)
    if a == "B":
        B.append(b)
    if a == "C":
        C.append(b)
    if a == "D":
        D.append(b)
    if a=="E":
        E.append(b)
for i in range(len(A)):
    if A.count(A[i])>0.1*T:
        print i
        break
    else:
        print "Nothing Unusual"
for i in A:
    if A.count(i)>0.1*T:
        print i
    else:
        print "Nothing Unusual"
for i in B:
    if B.count(i)>0.1*T:
        print i
    else:
        print "Nothing Unusual"
for i in C:
    if C.count(i)>0.1*T:
        print i
    else:
        print "Nothing Unusual"
for i in D:
    if D.count(i)>0.1*T:
        print i
    else:
        print "Nothing Unusual"
for i in E:
    if E.count(i)>0.1*T:
        print i
    else:
        print "Nothing Unusual"
    
    

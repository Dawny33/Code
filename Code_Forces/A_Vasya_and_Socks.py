x=raw_input()
n,m=x.split()
n=int(n)
m=int(m)
s=n
while(True):
    s=s+(n/m)
    d=(n/m)+n%m
    n=d
    if n<m:
        break
print s

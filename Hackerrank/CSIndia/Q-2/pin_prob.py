
T = int(input())


def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):    
    return a * b / gcd(a, b)



for _ in range(T):
    x=raw_input()
    n,m=map(int,x.split())
    x=raw_input()
    a=[]
    a=map(int,x.split())
    s=1
    l=len(a)
    for i in range(0,l):
        s=lcm(a[i],s)
    print n/s

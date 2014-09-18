
T = int(input())


def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):    
    return a * b // gcd(a, b)



for _ in range(T):
    s1 = map(int, raw_input().split())
    s2 = map(int, raw_input().split())
    arr = []

    if len(s2)==s1[1]:
        for i in range(1,len(s2)):
            arr.append(lcm(s2[i-1],s2[i]))
        if len(s2) == 1:
            print s1[0]/s2[0]
        else:
            print s1[0]/arr[-1]

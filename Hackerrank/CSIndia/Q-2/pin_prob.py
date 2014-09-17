
T = int(input())

def gcd(a,b):
 if a < b: a,b = b,a
 while a:
  a,b = b,a%b
 return b

def lcm(a,b):
 return (a*b)/gcd(a,b)



for _ in range(T):
    s1 = map(int, raw_input().split())
    s2 = map(int, raw_input().split())
    count = 0
    if len(s2)==s1[1]:
        i = 0
        while len(s2)>2:
            a = s2.pop(i)
            b = s2.pop(i+1)
            s2.append(lcm(a,b))
        print s2

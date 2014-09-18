def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    
    return a * b // gcd(a, b)



p = [5,10,15]
arr = []
i = 1
while i<len(p):
    arr.append(lcm(p[i-1],p[i]))
    i+=1

print arr[-1]

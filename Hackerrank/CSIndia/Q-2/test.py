def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    
    return a * b // gcd(a, b)

def lcml(p):
    for i in range(len(p)):
        return lcm(p[i],p[i+1:])


print lcml([2,3])

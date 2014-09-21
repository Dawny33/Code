import math

def nCr(n):
    return math.factorial(n) / math.factorial(6) / math.factorial(n-6)

T = int(input())

print nCr(T)%1000000007

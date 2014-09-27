import math

#Primalty check through the sieve of erosthenes
def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

T = int(input())
while(T):
    T -= 1
    s = int(input())
    i = 1
    count = 0
    while()

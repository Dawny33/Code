import math

T = int(input())

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors[:-1]:
        yield divisor

#print list(divisorGenerator(8))

def is_square(integer):
    root = math.sqrt(integer)
    if (int(root + 0.5) ** 2 == integer) and integer%2==0: 
        return True
    else:
        return False
    
def reducefract(n, d):
    '''Reduces fractions. n is the numerator and d the denominator.'''
    def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n
    assert d!=0, "integer division by zero"
    assert isinstance(d, int), "must be int"
    assert isinstance(n, int), "must be int"
    greatest=gcd(n,d)
    n/=greatest
    d/=greatest
    return n, d

while(T):
    T -= 1
    s = int(input())
    count = 0
    arr = list(divisorGenerator(s))
    for i in range(1,len(arr)):
        if is_square(arr[i])==True:

            count += 1
    if s<=2:
        print 0
    elif count == len(arr):
        print 1
    else:
        k = reducefract(count,len(arr))
        print str(k[0]) + "/" + str(k[1])


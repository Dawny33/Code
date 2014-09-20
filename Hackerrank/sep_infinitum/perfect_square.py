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
def rec_mult(li):
    prod = 1
    for j in range(len(li)):
        prod*li[j]
    return prod

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
        countgen = list(divisorGenerator(count))
        arrgen = list(divisorGenerator(count))
        for i in countgen:
            for j in arrgen:
                if i==j:
                    countgen.remove(i)
                    arrgen.remove(j)
                    
        if (len(countgen)>1 or len(countgen)) or (len(countgen)>1 and len(countgen)):
            print str(rec_mult(countgen)) + "/" + str(rec_mult(arrgen))
        else:
            print str(count) + "/" + str(len(arr))


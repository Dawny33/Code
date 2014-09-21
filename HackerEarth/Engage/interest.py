def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#print list(factors(6))

def f(n):
    count = 0
    if (n==1):
        return 0
    else:
        count += (f(n-1) + min(list(factors(n))))
        return count
        
        

print f(3)
    

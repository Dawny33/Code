T = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for _ in range(T):
    count = 0
    s = int(input())
    fact = factorial(s)
    #print fact
    fact = str(fact)
    #print fact
    for i in range(len(fact)):
        if fact[i] =="4" or fact[i]=="7":
            count += 1
    print count
    

def isprime(n):

    n = abs(int(n))

    if n < 2:
        return False

    if n == 2:
        return True
    
    if not n & 1:
        return False

    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True



s = "0"

i = 1

while(True):
    if isprime(i)==True:
        s.join("1")
    else:
        s.join("0")

    i += 1
    if i>33:
        break

print s

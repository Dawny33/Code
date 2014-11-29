def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        else:
            return True

T = input()
if prime(T):
    print "PRIME"
else:
    print "COMPOSITE"

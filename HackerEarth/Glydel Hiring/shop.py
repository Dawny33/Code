T = int(input())


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return sorted(primfac)


while(T):
    T -= 1

    s = int(input())
    print s-primes(s)[0]

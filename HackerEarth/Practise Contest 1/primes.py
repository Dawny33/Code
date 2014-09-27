def nth_prime(n):
    prime_list = []
    current = 2
    count = 0
    while(count < n):
        is_prime = True
        for prime in prime_list:
            if current % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(current)
            count += 1
        current += 1
    return current - 1

T = int(input())
while(T):
    T -= 1
    s = int(input())
    print nth_prime(s)

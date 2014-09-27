T = int(input())

while(T):
    T -= 1
    s = int(input())
    i = 1
    count = 0
    while(i<=s):
        if s%i == 0:
            count += 1
        i += 1

    print count

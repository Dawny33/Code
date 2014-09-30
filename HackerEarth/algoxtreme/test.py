def zeroes(n):
    i = 1
    result = 0
    while n >= i:
        i *= 5
        result += n/i  # (taking floor, just like Python or Java does)
    return result

T = int(input())

while(T):
    T -= 1
    s = map(int, raw_input().split())
    print s

    count = 0
    for i in range(s[0],s[1]):
        count +=  zeroes(i)
    print count

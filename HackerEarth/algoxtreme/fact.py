def zeroes(n):
    i = 1
    result = 0
    while n >= i:
        i *= 5
        result += n/i  
    return result

T = int(input())

while(T):
    T -= 1
    s = raw_input().split()
    s[0],s[1] = int(s[0]),int(s[1])
    #print s

    count = 0

    i = s[0]
    while (i<=s[1]):
        count +=  zeroes(i)
        i += 1
    print count

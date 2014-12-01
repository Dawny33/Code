import sys

T = input()
while(T):
    T -= 1
    p = input()
    s = [int(i) for i in sys.stdin.readline().split()]
    s = sorted(s)
    i = 0
    summ = 0
    j = len(s)-1
    while(i<j):
        summ += min(((pow(s[i],s[j])%1000000007)), ((pow(s[j],s[i])%1000000007)))
        i += 1
        j -= 1
    print summ

T = int(input())

for _ in range(T):
    T1 = int(input())
    s = map(int, raw_input().split())
    count = 0
    if T1==len(s):
        for i in range(len(s)-1):
            if s[i+1]>s[i]:
                count = s[i]-s[i+1]
            if s[i+1]<=s[i]:
                count = 0
    print count

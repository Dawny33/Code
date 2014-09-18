T = int(input())

count = 0

for _ in range(T):
    s = map(int, raw_input().split())
    if s[1]>=s[0]:
        if (s[1]-s[0]) >= 2:
            #print diff
            count = count+1

print count
        


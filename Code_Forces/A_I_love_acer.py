T = input()
s = [int(i) for i in raw_input().split()]
c = 0
i = 1
maxx = s[0]
minn = s[0]

for i in range(len(s)):
    if s[i]>maxx:
        maxx = s[i]
        c += 1

    if s[i]<minn:
        minn = s[i]
        c += 1
print c
        

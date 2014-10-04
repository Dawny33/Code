T = int(input())

while(T):
    T -= 1
    a,b = map(int, raw_input().split())
    s = []
    while(b):
        b -= 1
        c,d = map(int, raw_input().split())
        s.append((c,d))


c = 0
mm = []
mmm = []
for i in s:
    mm.append(i[0])
    mmm.append(i[1])
    minn = min(mm)
    maxx = max(mmm)
    if (minn in i) or (maxx in i):
        c += 1
if (1 and a) in i:
    c -= 1

print c

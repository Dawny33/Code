t = raw_input().split(" ")
n = int(t[0])
k = int(t[1])

s = raw_input().split(" ")
p = map(int, s)
count = 0

for i in p:
    if i >0 and i>=p[k-1]:
        count += 1

print count


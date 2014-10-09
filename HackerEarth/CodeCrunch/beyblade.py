T = input()

sc = 0


s = [int(i) for i in raw_input().split()]
summ = sum(s)
buff = []
for j in range(1,len(s)):
    if s[j-1]<s[j]:
        buff.append(s[j-1])
    else:
        sc += len(buff)*s[j]
        buff = []
print summ - sc

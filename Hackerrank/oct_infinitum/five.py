T = input()

s = [int(i) for i in raw_input().split()]
buff = []

i = 0
while(i<10*max(s)):
    if "11" not in str(bin(i)[2:]):
        buff.append(i)
        i += 1
    else:
        i += 1

xx = s[0]
for i in range(1,len(s)):
    xx ^= buff[s[i]]

print xx
    

from collections import Counter

T = int(input())

for _ in range(T):
    s = raw_input()
    c = Counter(s)
    s = sorted(c.values())[::-1]
    i = 1
    while(i<len(s)):
        if s[i-1]==s[i] and i!=len(s):
            i+=1
        else:
            if i!=len(s):
                p = s[i] - s[i+1]
            print p
            break
        i +=1

    
    #print sorted(c.values())[::-1][0]-sorted(c.values())[::-1][1]

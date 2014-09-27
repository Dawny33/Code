T = int(input())

s = map(int, raw_input().split())
count = 0

if (T==len(s)):
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j:
                if s[i]==s[j]:                     
                    count += 2
                else:
                    count = 0
    
    

    print count

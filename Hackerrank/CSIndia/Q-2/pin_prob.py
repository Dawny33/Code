T = int(input())

for _ in range(T):
    s1 = map(int, raw_input().split())
    s2 = map(int, raw_input().split())
    count = 0
    if len(s2)==s1[1]:
        for i in range(s1[0]):
            for j in range(len(s2)):
                if i%s2[j]==0:
                    count += 1
                    
    print count
    

T = int(input())

for _ in range(T):
    p = raw_input()
    p = map(int, p.split())
    while (len(p)<=T):
        for i in range(1,T-1):
            if p[i] >p[i+1] and p[i]>p[i-1]:
                p[i] = "X"

        print p
                

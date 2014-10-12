T = input()

while(T):
    T -= 1

    s = input()
    p = [int(i) for i in raw_input().split()]

    summ = 0
    neg = []
    #pp = p
    for x in range(len(p)):
        for j in range(len(p)):
            if p[x]<0 and p[j]>0:
                summ += (p[j]*(abs(x-j)))

                

    print summ
                

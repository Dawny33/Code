T = int(input())

while(T):
    T -= 1

    p,k = map(int, raw_input().split())

    j = k+1
    total = []

    arr = []
    for i in range(1, k+1):
        arr.append(j-i)
    #print arr
    
    while(True):
        for k in arr:
            print k-j
            if (k-j)>0:
                j += 1
            else:
                if (k-j)<0:
                    total.append(j)
                    j+=1
                else:
                    break
        if len(total) == p:
            break
        j += 1
    print total
                    
            

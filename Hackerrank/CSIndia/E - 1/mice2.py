T = int(input())

while(T):
    T-=1

    n,m = map(int, raw_input().split())

    t1 = map(int, raw_input().split())
    t2 = map(int, raw_input().split())

    arr = []
    if len(t1)==n and if len(t2)==m:
        i = 0
        while(i<=len(t1)):
            #for i in range(len(t1)):
            arr.append(abs(min(t1)-min(t2)))

            arr = map(abs(min(t1)-min(t2)))
            
            t1.remove(min(t1))
            t2.remove(min(t2))
                    #print arr
            i += 1

    print max(arr)

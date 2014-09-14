T = int(input())

for _ in range(T):
    num = int(input())
    if num!=0:
        arr = []
        t1 = map(int, raw_input().split())
        t2 = map(int, raw_input().split())
        if len(t1)==num and len(t2)==num:
            for i in range(num):
                arr.append(abs(t1[i]-t2[i]))
            #print arr
            print max(arr)

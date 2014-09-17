T = int(input())

for _ in range(T):
    s = map(int, raw_input().split())
    t = map(int, raw_input().split())
    if len(t) == s[1]:
        arr=[]
        for i in range(s[0]):
            for j in range(len(t)):
                #if i%t[j]==0:
                arr.append(i%t[j]==0)
    print arr
                

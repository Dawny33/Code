T = int(input())
s1 = map(int, raw_input().split())

T2 = int(input())
s2 = map(int, raw_input().split())

s1s = sum(s1)


for i in s2:
    c = 5
    for j in range(len(s1),0,-1):
        if s1[j-1]<= (s1s - s1[j-1]) <= s1s:
            print "Sum is", s1s - s1[j-1]
            c -= 1
        s1s -= s1[j-1]
            #break
    
    print c 

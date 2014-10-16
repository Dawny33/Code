T = input()

while(T):
    T -= 1

    G,M = [int(i) for i in raw_input().split()]
    buff = []
    s = [int(i) for i in raw_input().split()]
    s = sorted(s)
    while(sum(buff)<=M):
        buff.append(s[0])
        s = s[1:]
        #print buff

    if sum(buff)>M:
        print len(buff)-1
    else:
        print len(buff)
        

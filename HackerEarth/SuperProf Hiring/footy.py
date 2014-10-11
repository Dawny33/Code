T = input()

while(T):
    T -= 1
    buff = []
    a,b = [int(i) for i in raw_input().split()]
    
    buff.append(b)
    pt = 0
    while(a):
        a -= 1
        c = [i for i in raw_input().split()]
        if len(c)==2:
            c[1] = int(c[1])
        if c[0] == "P":
            buff.append(c[1])
            #pt = len(buff)-1
            k = len(buff)-1
            l = len(buff)-2
            #print buff[k]
            
        if c[0] == "B":
            k,l = l,k
            
        #print k
        print buff,buff[k]
        
print "Player " + str(buff[k])

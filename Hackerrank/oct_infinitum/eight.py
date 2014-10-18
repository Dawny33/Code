T = input()

while(T):
    T -= 1

    N,K,x,y = [int(i) for i in raw_input().split()]
    while(N):
        N -= 1
        while(K):
            s = [i for i in raw_input().split()]
            if s[0]=="T":
                a,b = int(s[1]),int(s[2])
                x = a+x
                y = y+x
            if s[0]=="S":
                c = int(s[1])
                x = c*x
                y = c*y
            if s[0]=="R":
                a,b = int(s[1]),int(s[2])
                x = a*x + b*y
                y = a*y - b*x
            if s[0]=="F":
                if s[1]=="X":
                    y = -x
                else:
                    x = -x
            if s[0]=="I":
                if x==0 and y==0:
                    print "WONDERLAND"
                else:
                    x = (x/(x**2 + y**2))
                    y = (y/(x**2 + y**2))
            
            K -= 1
    
                

T = input()

while(T):
    T -= 1

    R,G,B, M = [int(i) for i in raw_input().split()]
    r = [int(i) for i in raw_input().split()]
    g = [int(i) for i in raw_input().split()]
    b = [int(i) for i in raw_input().split()]
    sumr = sum(r)
    sumg = sum(g)
    sumb = sum(b)


    while(M):
        M -= 1
        if sumr>sumg and sumr>sumb:
            rn = [x / 2 for x in r]
            r = rn
            sumr = sum(r)
        #print max(r+g+b)

        if sumg>sumr and sumg>sumb:
            gn = [y / 2 for y in g]
            g = gn
            sumg = sum(g)
        #print max(r+g+b)

        if sumb>sumg and sumb>sumr:
            bn = [z / 2 for z in b]
            b = bn
            sumb = sum(b)
        #print max(r+g+b)

    print max(r+g+b)

    

    
    
        
            

            
        

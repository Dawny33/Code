T = int(input())

while(T):
    T -= 1
    l,b,d = map(int,raw_input().split())

    if (d>l) or (d>b):
        print 0
        
    elif (l%d==0) and (b%d==0):
        print ((l/d)*(b/d))%1000000007

    elif (l%d==0) and (b%d>0):
        print ((l/d)*((b-1)/d))%1000000007
        
    elif (l%d>0) and (b%d==0):
        print (((l-1)/d)*(b/d))%1000000007

    elif (l%d>0) and (b%d>0):
        print (((l-1)/d)*((b-1)/d))%1000000007

    else:
        print (((l/d)*(b/d)))%1000000007

    

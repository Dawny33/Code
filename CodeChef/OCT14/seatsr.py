T = input()

while(T):
    T -= 1

    s = raw_input()
    w = raw_input()
    
    a,b,k = [int(i) for i in raw_input().split()]
    c = 0
    if s!= w:
        
        if len(s)==len(w):
                for i in range(len(s)):
                    if s[i]!=w[i]:
                        if a>=b:
                            c += b
                        else:
                            c += a
                        
        if len(s) != len(w):
            c += a*abs(len(s)-len(w))
        
    
    if c<k:
        print c
    else:
        print -1
        
                

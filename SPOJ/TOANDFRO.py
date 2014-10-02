
while(True):
    a=input()
    if a==0:
        break
    
    n=raw_input()
    
    k=0
    b=[]    
    j=0
    
    while j<len(n):
        if k%2:
            b.append(n[j+a-1:j-1:-1])
        else:
            b.append(n[j:j+a])
    j+=a
    k+=1
    s=""
    
    for k in range(a):
        for i in b:
            s+= i[k]
    print s

T = input()

arr = []
while(T):
    T -= 1
    
    s = input()
    arr.append(s)

#print arr

if sum(arr) > 0:
    print "first"
if sum(arr) < 0:
    print "second"

def lex(a,b):
    if len(a)>len(b):
        #return True
        for i in range(len(a)):
            for j in range(len(b)):
                if i == j:
                    if a[i]== abs(b[j]):
                        return True
    else:
        r = min(len(a), len(b)) - 1
        for i in range(r):
            for j in range(r):
                if i==j and a[r]> abs(b[r]):
                    if a[i] == abs(b[j]):
                        return True
                            

if sum(arr) == 0:
    pos = []
    neg = []
    for i in xrange(len(arr)):
        if arr[i]<0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
            
    #print pos
    #print neg

    if lex(pos,neg)== True:
        print "first"
    else:
        print "second"
    

T = raw_input()

flag = 0
#first = 0
op = 0
for i in range(flag+1,len(T)):
    if T[i] == flag:
        op += 1
    else:
        flag = i
if op>=7:
    print "YES"
else:
    print "NO"    

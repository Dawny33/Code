T = input()

s = raw_input()

while(T):
    T -= 1
    p = raw_input()
    s  = s.replace(p,'')

if len(s)==0:
    print 0
else:
    print s

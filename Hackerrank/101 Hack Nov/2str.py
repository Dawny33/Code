T = input()

def h(a, b):
        return not set(a).isdisjoint(b)
    
while(T):
    T -= 1
    s = raw_input()
    p = raw_input()
    if h(s,p):
        print "YES"
    else:
        print "NO"

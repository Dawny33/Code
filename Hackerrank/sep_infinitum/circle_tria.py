T = int(input())

def disin(x,y,x_center,y_center,radius):
    return (((x - x_center)**2 + (y - y_center)**2) < radius**2)

def disout(x,y,x_center,y_center,radius):
    return (((x - x_center)**2 + (y - y_center)**2) > radius**2)


while(T):
    T -= 1
    s = map(int,raw_input().split())
    t1 = map(int,raw_input().split())
    t2 = map(int,raw_input().split())
    t3 = map(int,raw_input().split())

    #Condition for all in
    if (disin(t1[0],t1[1],s[0],s[1], s[2])==True) and (disin(t2[0],t2[1],s[0],s[1], s[2])==True) and (disin(t3[0],t3[1],s[0],s[1], s[2])==True):
        print "NO"

    #Condition for all out
    elif (disout(t1[0],t1[1],s[0],s[1], s[2])==True) and (disout(t2[0],t2[1],s[0],s[1], s[2])==True) and (disout(t3[0],t3[1],s[0],s[1], s[2])==True):
        print "NO"

    else:
        print "YES"

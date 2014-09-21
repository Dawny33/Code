T = int(input())

def disin(x,y,x_center,y_center,radius):
    return (((x - x_center)**2 + (y - y_center)**2) < radius**2)

def disout(x,y,x_center,y_center,radius):
    return (((x - x_center)**2 + (y - y_center)**2) > radius**2)

while(T):
    T -= 1
    xc,yc,r = map(int,raw_input().split())
    x1,y1 = map(int,raw_input().split())
    x2,y2 = map(int,raw_input().split())
    x3,y3 = map(int,raw_input().split())

    #Condition for all in
    if (disin(x1,y1,xc,yc,r)==True) and (disin(x2,y2,xc,yc,r)==True) and (disin(x3,y3,xc,yc,r)==True):
        print "NO"

    #Condition for all out
    elif (disout(x1,y1,xc,yc,r)==True) and (disout(x2,y2,xc,yc,r)==True) and (disout(x3,y3,xc,yc,r)==True):
        print "NO"
 
    else:
        print "YES"

import math

T = input()

while(T):
    T -= 1
    day = input()
    prob = input()

    if day==1 or day==3 or day==5 or day==7 or day == 8 or day==10 or day==12:
        print int(31*prob)
        print int(31*prob*2500*3)
    if day==2:
        print int(30*prob)
        print int(28*prob*2500*3)
    if day==4 or day==6 or day==9 or day==11:
        print int(30*prob)
        print int(30*prob*2500*3)

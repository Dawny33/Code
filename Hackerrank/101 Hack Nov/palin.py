import sys
T = input()

while(T):
    T -= 1
    s = [int(i) for i in sys.stdin.readline().split()]
    a = s[0]
    b = s[1]
    #print a
    #print b
    #if a<=2:
    print (pow(b,a) - (b))%1000000007
    #else:
        #print (pow(b,a) - (2*b))%1000000007

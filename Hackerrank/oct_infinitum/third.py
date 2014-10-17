T = input()

while(T):
    T -= 1
    a,b,x = [int(i) for i in raw_input().split()]

    if b>0:
        print pow(a,b)%x
    else:
        print int(pow((pow(a,-1)%x),b))

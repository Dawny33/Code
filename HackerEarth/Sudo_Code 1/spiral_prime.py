T = input()

while(T):
    T -= 1
    s = input()
    s2 = s/2
    s3 = s/2
    #print s2
    summ = 3
    while(s2):
        i = 4
        #summ = 3
        while(i):
            summ += (2*s2+1)
            #print summ
            summ = summ
            i -= 1
        s2 -= 1

    print summ

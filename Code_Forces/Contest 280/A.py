T = input()

i = 1
summ = 0
x = i
while(i):
    #j = i
    summ += i
    x += summ 
    #print summ
    #i += 1
    #if i==10:
        #break
    if T == 1:
        print 1
        break
    if x == T:
        print i+1
        break
    if x > T:
        print i-1
        break
    i += 1

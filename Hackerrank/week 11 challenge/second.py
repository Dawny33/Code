def strange(N):
    count = len(str(N))
    if count == 1:
        return True
    if N%count == 0 and strange(N/count) == True:
        return True
    

T = input()

while(T):
    T -=1
    a,b = [int(x) for x in raw_input().split()]
    co = 0
    while(a<=b):
        if strange(a)==True:
            co += 1
            a += 1
        else:
            a += 1
    print co

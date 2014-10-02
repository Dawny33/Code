T = int(input())

while(T):
    T -= 1

    s = int(input())
    i = s+1
    while(i):
        k = str(i)
        if k[:]==k[::-1]:
            print k
            break
        else:
            i += 1

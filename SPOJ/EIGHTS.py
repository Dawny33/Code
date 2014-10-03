T = int(input())

while(T):
    T -= 1

    s = int(input())

    j = 0
    i = s-1
    while True:
        if str(i**3)[-3:] == "888":
            print j
            break
        else:
            j += 1
            i += 1

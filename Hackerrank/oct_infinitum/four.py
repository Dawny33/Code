buff = []

T = input()
while(T):
    T -= 1
    buff.append(input())


D = input()
while(D):
    D -= 1
    c = 0
    l,r = [int(i) for i in raw_input().split()]
    for i in range(l,r+1):
        for j in range(len(buff)):
            if i%buff[j]:
                c += 1

    print c

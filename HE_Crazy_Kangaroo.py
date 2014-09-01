T = raw_input()
T = int(T)

for _ in range(T):
    count = 0
    p = raw_input().split()
    p = int(p)
    for i in range(p[0], p[1]+1):
        if i%p[2]==0:
            count += 1

    print count

import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N,C,M = list(int(x) for x in sys.stdin.readline().split())
    t = N // C
    w = t
    while w >= M:
        w += 1-M
        t += 1
    print(t)







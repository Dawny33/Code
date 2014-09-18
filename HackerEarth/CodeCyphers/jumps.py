T = int(input())

for _ in range(T):
    s = map(int, raw_input().split())
    if s[0]<=5:
        if s[1] == 0:
            print s[0]-1
        else:
            print ((4*s[1]) + (5-s[0]))

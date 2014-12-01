T = input()
while(T):
    T -= 1
    c = 0
    s = raw_input().strip("0")
    for i in range(len(s)):
        if s[i]==0:
            s.remove(s[i])
        if int(s)%int(s[i]) == 0:
            c += 1

    print c

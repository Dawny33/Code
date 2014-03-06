T = int(input())

for i in range(T):
    t = input()
    count = 0
    for x in range(len(t)):
        if (t[x]=='A')or(t[x]=='D')or(t[x]=='O')or(t[x]=='P')or(t[x]=='R')or(t[x]=='Q'):
            count  = count+ 1
        elif (t[x] == 'B'):
            count =count+ 2
    print(count)

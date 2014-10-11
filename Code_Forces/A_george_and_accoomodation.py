T = input()

c = 0
while(T):
    T -= 1
    s = [int(i) for i in raw_input().split()]
    if s[1]-s[0]>=2:
        c += 1

print c
    
        


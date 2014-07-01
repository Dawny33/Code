T=int(raw_input())
x=0
for _ in range(T):
    t=raw_input()
    if(t[1]=='+'):
        x+=1
    else:
        x-=1
print x

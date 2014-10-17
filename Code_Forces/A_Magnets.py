T = input()

buff = []
c = 0
while(T):
    T -= 1
    
    s = raw_input()
    if len(buff)==0:
        buff.append(s)
    else:
        if s!=buff[len(buff)-1]:
             c += 1
             buff.append(s)

print c+1

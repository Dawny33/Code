import sys

p = raw_input()
q = raw_input()

p1 = {}
p2 = {}

T = input()
while(T):
    T -= 1
    r = [i for i in sys.stdin.readline().split()]
    if r[1] == "h":
        if p1[r[2]] != []:
            if p1[r[2]][2]=="y":
                p1[r[2]][2] = "r"
        else:
            p1[r[2]] = (r[0],r[2],r[3])
        
    if r[1] == "a":
        if p2[r[2]][2]=="y":
            p2[r[2]][2] = "r"
        else:
            p2[r[2]] = (r[0],r[2],r[3])
        p2[r[2]] = (r[0],r[2],r[3])

print p1
print p2

for i in range(len(p1.values())):
    if i[2] == "r":
        print p + str(p1[i][1]) + str(p1[i][0])

for i in range(len(p1.values())):
    if i[2] == "r":
        print q + str(p2[i][1]) + str(p2[i][0])
    
        
        

    

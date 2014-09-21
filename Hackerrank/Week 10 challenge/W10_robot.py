import random

N = input()

def go(step,energy):
    score = 0
    if step==N:
        #print V
        score += V[step-1]
        return score
    else:
        way = random.randint(1,2)
        if way==1:
            score += V[step-1]
        else:
            energy = P[step-1]
        if energy>0:
            go(step+1, energy-1)
        else:
            return 20
    return score
    


V = []
P = []
go_arr = []
for _ in range(N):
    v,p = map(int, raw_input().split())
    V = V + [v]
    P = P + [p]

for i in range(0,len(V)-1):
    go_arr.append(go(V[i],P[i]))

print max(go_arr)+N


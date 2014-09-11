import random

N = input()

def go(step,energy):
    score = 0
    if step==N:
        score += V[step]
    else:
        way = random.randint(1,2)
        if way==1:
            score += V[step]
        else:
            energy = P[step]
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
    V = V.append(v)
    P = P.append(p)
    go_arr.append(go(v,p))
    print max(go_arr)

print V
print P


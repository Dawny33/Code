import random

N = input()

V = []
P = []
go_arr = []
for _ in range(N):
    s = map(int, raw_input().split())
    V = V.append(s[0])
    P = P.append(s[1])
    go_arr.append(go(s[0],s[1]))
    print max(go_arr)

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
    


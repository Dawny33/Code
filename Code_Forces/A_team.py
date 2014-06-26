N = raw_input()
N = int(N)

count = 0
for _ in range(0,N):
    T = raw_input().split(" ")
    p1 = int(T[0])
    p2 = int(T[1])
    p3 = int(T[2])
    if p1 and p2 ==1:
        count +=1
    elif p1 or p2 == 1:
        if p3 == 1:
            count += 1

print count






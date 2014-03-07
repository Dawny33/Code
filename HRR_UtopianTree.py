N = int(input())

for _ in range(N):
    x = int(input())
    height =1
    for i in range(x):
        if i%2==0:
            height *= 2
        elif i%2!=0:
            height += 1
    print(height)
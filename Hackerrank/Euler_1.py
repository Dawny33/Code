T = int(input())
sum = 0
for _ in range(0,T):
    p = int(input())
    for i in range(0,p):
        if (i%3==0) or (i%5==0):
            sum = sum + i
    print(sum)        

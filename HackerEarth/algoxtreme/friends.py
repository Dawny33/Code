
n,m,a,b = map(int, raw_input().split())

arr = []
count = 0
for i in range(n+1):
    for j in range(n+1):
        if i!=j:
            arr.append((i,j))

#print len(arr)
while(m):
    m -= 1
    x,y = map(int,raw_input().split())
    tup = (x,y)
    arr.remove(tup)

#print arr
#print len(arr)

for i in range(len(arr)):
    #print i
    if a == arr[i][0]:
        count += 1
    if b == arr[i][1]:
        count += 1

print count

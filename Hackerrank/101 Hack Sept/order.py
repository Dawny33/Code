T = int(input())

arr = []
dirr = {}

while(T):
    T-=1
    a,b = map(int, raw_input().split())
    arr.append(a+b)

arr2 = sorted(arr)
fin = []
for i in range(len(arr2)):
    for j in range(len(arr)):
        if arr[i] == arr2[j]:
            fin.append(j+1)    
    
#print arr
#print arr2
print reduce(lambda x, y: str(x) + " "+ str(y), fin)

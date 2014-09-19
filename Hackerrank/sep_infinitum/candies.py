T = int(input())

for _ in range(T):
    s = int(input())
    arr = []
    arr2 = []
    count = 0
    for i in range(1,(s/2)):
        arr.append(i**2)
    sums = 0
    #print arr
    for j in range(len(arr)):
        if sums <= s:
            sums += arr[j]
            arr2.append(arr[j])
    if s==1:
        print 1
    elif sums>s:
        print len(arr2)-1
    else:
        print len(arr2)

T = int(input())

arr = []
while(T):
    T -= 1

    s = raw_input()
    arr.append(s)

arr = set(arr)
arr = sorted(arr)

print len(arr)
for j in arr:
    print j

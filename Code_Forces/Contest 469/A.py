T = int(input())

s1 = map(int, raw_input().split())
s2 = map(int,raw_input().split())

arr = []
if (len(s1[1:])==s1[0]) and (len(s2[1:])==s2[0]):
    arr = arr + s1[1:]
    arr = arr + s2[1:]
#print arr

arr2 = []
for i in range(T):
    arr2.append(i)

arr3 = []

for j in set(arr):
    arr3.append(j)

if len(arr3) == len(arr2):
    print "I become the guy."
else:
    print "Oh, my keyboard!"


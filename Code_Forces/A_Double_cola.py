from math import ceil
s = int(input())
names = ["Sheldon","Leonard","Penny","Rajesh","Howard"]

i = 0
j = 1
k = len(names)

while(i<=s):
    i += k
    k += k
    j += j

print names[int(ceil((s - (i - k * 0.5)) / (j * 0.5)) - 1)]

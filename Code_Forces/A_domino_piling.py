T = raw_input().split(" ")

i = int(T[0])
j = int(T[1])

if i%2 == 0:
    ans = (i/2)*j
else:
    if j%2 == 0:
        ans = ((i-1)/2)*j + ((j)/2)
    else:
        ans = ((i-1)/2)*j + ((j-1)/2)


print ans
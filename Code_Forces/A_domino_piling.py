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

#This is also an example of a greedy algorithm implementation.

#We first deal with the case when M is even. Then, the formula is simply (M/2)*N
# But when M is odd, there are still two more cases, one when N is even and two, when N is odd.

#Case 1: when N is even, then we greedily deal with (M-1)XN portion of the board, and fill it up and then we deal with the remaining strip.
#So, the formuula is ((M-1)/2)*N + (N/2)

#Case2: when N is also odd, then we approach it similarly, but this time one block gets left over. So, the formula is ((M-1)/2)*N + ((N-1)/2),
#as we break the columns also into N-1 and deal with the even portion first.
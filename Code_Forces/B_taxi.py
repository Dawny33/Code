T = raw_input()
T = int(T)

inp = raw_input().split(" ")
inp.sort(reverse = True)
inp = [int(i) for i in inp]

summ = 0
i = 0
j = len(inp) - 1

while i <=j:
    summ += 1
    resid = 4 - inp[i]
    while (inp[j] <= resid) and (j>=i):
        resid -= inp[j]
        j -= 1
    i += 1

print summ

#Consider an example [1,2,4,3,3]
# Greedy  algorithm works like this:
#Take in the maximum item first in the reverse sorted list: [4,3,3,2,1]

#Now, we have i as 4 and j as 1. So, residual is 0. So, it does not enter the second loop.
#Then we have 3. As inp[j](--> 1) < resid(--> 1), resid would be 0 after decrementing. So, count = 2
#The procedure goes on.

#Remember, if only the second loop is satisfied, the last(least) number is included, else the biggest numbers are taken in (Greedy, ain't it!)

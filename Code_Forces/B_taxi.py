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

from itertools import permutations

T = int(input())


for _ in range(T):
    s = raw_input()
    set_arr = []
    perms = [''.join(p) for p in permutations(s)]
    for j in set(perms):
        set_arr.append(j)
    sor_set_arr = sorted(set_arr)
    fin_arr = []
    for k in range(len(sor_set_arr)):
        if sor_set_arr[k]>s:
            fin_arr.append(sor_set_arr[k])
    if len(fin_arr)>0:
        print fin_arr[0]
    else:
        print "no answer"


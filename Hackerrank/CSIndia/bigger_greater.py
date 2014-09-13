
from itertools import permutations

T = int(input())

for _ in range(T):
    s = raw_input()
    set_arr = []
    perms = [''.join(p) for p in permutations(s) if p>s]
#    for j in set(perms):
#        set_arr.append(j)
#    sor_set_arr = qsort1(set_arr)
    fin_arr = []
    for k in range(len(perms)):
        if perms[k]>s:
            fin_arr.append(perms[k])
    if len(fin_arr)>0:
        print fin_arr[0]
    else:
        print "no answer"




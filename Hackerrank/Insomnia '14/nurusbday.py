import itertools
import timeit

T = int(input())

def a(data):
    return all(b <= a for a, b in itertools.izip(data, itertools.islice(data, 1, None)))

def qsort(inlist):
    if a(inlist) == True:
        return 0
    else:
        count = 0
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x > pivot])
        count += 1
        greater = qsort([x for x in inlist[1:] if x <= pivot])
        count += 1
        return count
            

    

while(T):
    T -= 1

    s = int(input())
    p = map(int, raw_input().split())
    if len(p)==s:
        print qsort(p)

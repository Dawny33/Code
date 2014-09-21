from itertools import chain, combinations

T = int(input())


def powerset(iterable):
  xs = list(iterable)
  return chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) )

#print list(powerset([1,2,3]))


while (T):
    T -= 1
    s = int(input())
    arr = []
    for i in range(1,s+1):
        arr.append(i)
    count = 0
    
    for i in list(powerset(arr)):
        for j in i:
            count += j

    print count

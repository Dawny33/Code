from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subsets(s):
    return map(set, powerset(s))

for i in powerset([1,2,3,4]):
    print sum(i)

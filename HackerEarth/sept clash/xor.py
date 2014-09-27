from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subsets(s):
    return map(set, powerset(s))

#for i in powerset([1,2,3,4]):
#    print sum(i)



T = int(input())

s = map(int, raw_input().split())

if len(s)==T:
    summ = []
    for i in powerset(s):
        #print i
        summ.append(sum(i))
#print summ

T2 = int(input())
while(T2):
    T2 -= 1
    p = int(input())
    for j in range(len(summ)):
        if (p ^ summ[j]) == 0:
            
            print str(summ[j]) + " " + str(summ.count(summ[j]))
            
            
            
        

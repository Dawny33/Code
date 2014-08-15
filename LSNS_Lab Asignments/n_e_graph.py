import random
import numpy as np
import math
import itertools
import matplotlib.pyplot as plt


def graph(n,e):
    m = np.zeros([n,n], int)

    k = 0
    
    while k<e:
        i = random.randrange(0,n)
        j = random.randrange(0,n)
        if i != j and m[i][j]==0:   
            m[i][j] = 1
            m[j][i] = 1
            k += 1
    #return m


#For calculating the degree of each node.
    degree = []
    for ij in m:
        summ =  0
        
        for ik in ij:
            summ += ik
        degree.append(summ)
    print degree
    plt.hist(degree)
    return m


#For calculating the average clustering coeffiecient.
def l(a,i,r):
    s=[b for b in r if a[i][b]]
    k=len(s)
    if k<2:
        return 0
    return 2.0*sum(map(lambda x:a[x[0]][x[1]],itertools.combinations(s,2)))/k/(k-1)

def g(a):
    no=len(a)
    r=range(no)
    return sum([l(a,i,r) for i in r])/no


print g(graph(10,8))		


#For the degree frequency plotting. Plot command in graph module.
plt.show()

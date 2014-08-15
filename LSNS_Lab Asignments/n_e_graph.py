import random
import numpy as np
import math
import itertools

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

##    for p in range(n):
##        summ = 0         
##        for q in range(n):            
##            summ += m[p][q]
##    
##            
##    return (summ,p)

    #print m

#For calculating the degree of each node.        
    for ij in m:
        summ =  0
        degree = []
        for ik in ij:
            summ += ik
        print summ    
    return m
        
print graph(10,8)
		

import itertools

N = int(input())

K = int(input())

k1_arr = []
k1 = map(int,raw_input().split())

for i in range(len(k1)):
    k1_arr.append(k1[i])


#print k1_arr
if(len(k1_arr)<=K):
    kk = list(itertools.permutations(k1_arr, K))
    print kk
    print kk[1]
        

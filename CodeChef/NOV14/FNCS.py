import sys

N = input()

num_arr = [int(i) for i in sys.stdin.readline().split()]

tup_arr = []
while(N):
    N -= 1
    m,n = [int(i) for i in sys.stdin.readline().split()]
    tup_arr.append((m,n))



#print tup_arr[0][0]

T = input()
while(T):
    T -= 1
    func_arr = [int(i) for i in sys.stdin.readline().split()]
    if func_arr[0] == 1:
        num_arr[func_arr[1]-1] = func_arr[2]
        
    if func_arr[0] == 2:
        summ = 0
        for j in xrange(func_arr[1]-1,func_arr[2]):
            #print tup_arr[j]
            summ += sum(num_arr[(tup_arr[j][0]-1):(tup_arr[j][1])])
        print summ
    

T = int(input())


for _ in range(T):
    t = raw_input().split()
    ord_mat = [int(i) for i in t[1:]]
    #print sorted(ord_mat)
    mean = sum(sorted(ord_mat))/len(sorted(ord_mat))
    sor_lis = sorted(ord_mat)
    new_l = []
    for i in range(len(sor_lis)):
        if sor_lis[i]>mean:
            new_l.append(sor_lis[i])
    print len(new_l)
    
    

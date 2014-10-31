T = input()
dic = {}
while(T):
    T -= 1

    s = [i for i in raw_input().split()]
    dic[s[0]] =[float(s[1])]
    dic[s[0]].append(float(s[2]))
    dic[s[0]].append(float(s[3]))


p = raw_input()

#print dic[p]



avg = sum(dic[p])/len(dic[p])
print ("%.2f" %avg)

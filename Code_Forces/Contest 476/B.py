s = raw_input()
w = raw_input()

c = 0
for i in range(len(s)):
    if s[i]=="+":
        c += 1
    if s[i] == "-":
        c -= 1

buff = []
ct = 0
cn = 0
for k in range(len(w)):
    if w[k] == "?":
        cn +=1
for j in range(len(w)):
    if w[j]=="+":
        ct += 1
    if w[j] == "-":
        ct -= 1
    if w[j] == "?":
        ct += 1
        buff.append(cn*ct)
        ct -= 1
        buff.append(cn*ct)

pq = 0
if c==ct:
    print  ("%.9f" %1.0)
else:
    for p in range(len(buff)):
        if buff[p]==c:
            pq += 1

    print ("%.9f" %round((pq*1.0)/len(buff),9))



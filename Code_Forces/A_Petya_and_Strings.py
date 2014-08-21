T = raw_input()
P = raw_input()
P = P.lower()

sum1 = 0
for i in range(len(T)):
    sum1 += ord(T[i])

sum2 = 0
for j in range(len(P)):
    sum2 += ord(P[j])


if sum1<sum2:
    print "-1"

elif sum1>sum2:
    print "1"

else:
    print "0"

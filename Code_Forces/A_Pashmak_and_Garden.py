T = raw_input()
T = map(int,T.split())


if (T[1]==T[3]) and (T[0]!=T[2]):
    p = T[2] - T[0]
    print str(T[0])+" "+str(T[1]+p)+" "+str(T[2])+" "+str(T[3]+p)

elif (T[0]==T[2]) and (T[1]!=T[3]):
    p2 = T[3] - T[1]
    print str(T[0]+p2)+" "+str(T[1])+" "+str(T[2]+p2)+" "+str(T[3])





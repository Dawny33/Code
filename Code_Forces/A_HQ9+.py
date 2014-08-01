T = raw_input()

for i in range(0, len(T)):
    if (T[i] == "H") or (T[i] == "Q") or (T[i] == "9") or (T[i] == "+"):
        print "YES"
        break
    else:
        print "NO"
        break

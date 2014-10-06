strr = "qwertyuiopasdfghjkl;zxcvbnm,./"


s = raw_input()

r = raw_input()

op = ""
for i in range(len(r)):
    for j in range(len(strr)):
        if s == "R":
            if r[i] == strr[j]:
                op += strr[j-1]
        else:
            if r[i]==strr[j]:
                op += strr[j+1]

print op

T = int(input())

for _ in range(T):
    s = raw_input()
    ord_mat = []
    rev_mat = []
    str_buff = ""
    for i in range(len(s)):
        ord_mat.append(s[i])
    #print ord_mat
    for j in reversed(sorted(ord_mat)):
        rev_mat.append(j)
        print rev_mat
    #for k in range(len(rev_mat)):
     #   str_buff = str_buff.join(rev_mat[k])
    if s == str_buff:
        print "no answer"
    else:
        print str_buff

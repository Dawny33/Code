T = input()

def is_palin(strr):
    if strr == strr[::-1]:
        return True

while(T):
    T -= 1

    s = raw_input()


    if is_palin(s)==True:
        print "YES"
    else:
        i,j = 0,len(s)-1
        while(i<j):
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                if is_palin(s[0:i]+s[i+1:])==True:
                    print "YES"
                    break
                elif is_palin(s[0:j]+s[j+1:])==True:
                    print "YES"
                    break
                else:
                    print "NO"
                    break
        
    





    
    if is_palin(s)==True:
        print "YES"
    else:
        for i in range(0,len(s)):
            if is_palin(s[0:i]+s[i+1:])==True:
                print "YES"
                break
        else:
            print "NO"







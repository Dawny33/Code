s = raw_input()


T = int(input())

while(T):
    T -= 1

    a,b = map(int, raw_input().split())

    if a>(len(s)-1) or b>(len(s)-1):
        s += s
        
    if s[a-1]==s[b-1]:
        print "Yes"
    else:
        print "No"

     

T = input()

while(T):
    T -= 1
    s = input()
    s = str(oct(s))
    if s == s[::-1]:
        print 1
    else:
        print -1

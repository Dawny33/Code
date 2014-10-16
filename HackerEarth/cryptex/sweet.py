import random
T = input()

def l(s):
    if all(x == s[0] for x in s)==True:
        return s[0]
    else:
        for i in range(len(s)):
            for j in range(len(s)):
                if i!=j:
                    if s[i]>s[j]:
                        s[i]=s[i]-s[j]
                    elif s[i]<s[j]:
                        s[j]=s[j]-s[i]
        return l(s)
        
    


while(T):
    T -= 1

    p = input()
    s1 = [int(i) for i in raw_input().split()]
    if len(s1)==p:
        print l(s1)

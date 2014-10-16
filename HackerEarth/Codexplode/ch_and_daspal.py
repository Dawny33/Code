import re

T = input()

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

while(T):
    T -= 1
    s = raw_input()
    c = 0
    for i in range(1,len(s)):
        if len(s)==1:
            c += 0
        else:
            l = findOccurences(s, s[i-1])
            if len(l)==1:
                c += 0
            else:
                c += 2**(max(l)-l[0])
    print c

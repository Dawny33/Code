import sys

T = input()
s = [int(i) for i in sys.stdin.readline().split()]

T1 = input()
s1 = [int(i) for i in sys.stdin.readline().split()]

c = 0

k = 0
j = 0
while(k):
    while(j):
        if (abs(s[k]-s1[j]) == 1):
            c += 1
            s.remove(s[k])
            s1.remove(s1[j])
            k += 1
            j+=1

            

            
print c

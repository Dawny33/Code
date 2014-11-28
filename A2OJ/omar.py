import sys
T = input()

while(T):
    T -= 1
    a,b = [int(i) for i in sys.stdin.readline().split()]
    print a+b

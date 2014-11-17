import sys
T = input()

while(T):
    T -= 1
    s = input()
    p = [int(i) for i in sys.stdin.readline().split()]

    print min(p)*s

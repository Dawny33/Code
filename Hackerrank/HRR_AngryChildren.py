import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
x = sorted(int(sys.stdin.readline()) for _ in range(N))

print(min(x[i+K-1] - x[i] for i in range(0,N-K-1)))


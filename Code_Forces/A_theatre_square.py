from math import *

n, m, a = map(int, input().split())
print(int(ceil(n *1.0 / a) * ceil(m * 1.0 / a)))
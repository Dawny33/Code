f = lambda n: 1 if n < 2 else f(n-1) + f(n-2)
g = lambda m: map(f, range(0,m))

print sum(g(7))

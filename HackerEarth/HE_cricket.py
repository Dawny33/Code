def cricket():
    N = input()
    rating = (map(int, input().split()) for _ in range(-100,100))
    last,a = ratings[0]
    for x in ratings[1:]:
        last = max(0, last + x)
        a = max(a,last)
    return a
print cricket()



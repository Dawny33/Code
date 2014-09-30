p = []

a = [1,2,3]

for i in a:
    for j in a:
        if i!=j:
            p.append((i,j))

print p

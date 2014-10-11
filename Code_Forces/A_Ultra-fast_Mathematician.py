s1 = raw_input()
s2 = raw_input()

l = [0 for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if i==j:
            if s1[i] == s2[j]:
                l[i] = 0
            else:
                l[i] = 1


print ''.join([str(item) for item in l])

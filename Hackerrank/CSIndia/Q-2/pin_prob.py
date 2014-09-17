
T = int(input())


def lcm(*values):
	values = set([abs(int(v)) for v in values])
	if values and 0 not in values:
		n = n0 = max(values)
		values.remove(n)
		while any( n % m for m in values ):
			n += n0
		return n
	return 0
#print lcm(*[2,3])



for _ in range(T):
    s1 = map(int, raw_input().split())
    s2 = map(int, raw_input().split())
    if len(s2)==s1[1]:
#    print s2
        lcm = lcm(*s2)
        print s1[0]/lcm

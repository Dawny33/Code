import itertools

T = input()

for _ in range(T):
    s = raw_input()
    dele = 0
    print len(s) - len(''.join(ch for ch, _ in itertools.groupby(s)))

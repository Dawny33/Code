def mssl(x):
    max_ending_here = max_so_far = 0
    for a in x:
        max_ending_here = max(0, max_ending_here + a)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

T = input()
while(T):
    T -=1
    l = input()
    s = [int(i) for i in raw_input().split()]
    print mssl(s)

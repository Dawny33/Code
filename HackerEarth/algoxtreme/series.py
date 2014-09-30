


T = int(input())

while(T):
    T -= 1
    q = map(int, raw_input().split())
    n = int(input())

    def s(n,arr=q):
        if n<5:
            return arr[n]
        else:
            return (s(n-1) + s(n-2) + s(n-3) + 2*s(n-4) + s(n-5))
    
    print s(n,q)
    


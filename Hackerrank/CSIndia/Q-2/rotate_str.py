
T = int(input())

for _ in range(T):
    s = raw_input()
    arr = []
    for i in range(len(s)):
        arr.append(s[-i:]+s[:-i])

    print max(arr)

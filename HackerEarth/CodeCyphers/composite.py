T = int(input())

import math
def is_prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

for _ in range(T):
    s = map(int, raw_input().split())
    arr = []
    count = 0
    for i in range(s[0], s[1] +1):
        if is_prime(i) == False:
            arr.append(i)
    for j in range(len(arr)):
        arr[j] = str(arr[j])
        if "7" in arr[j]:
            count += 1
    if count == 0:
        print -1
    else:
        print count

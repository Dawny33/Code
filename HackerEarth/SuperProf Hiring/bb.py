import math

def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n / 10
   return r


T = input()
while(T):
    T -= 1
    s = input()

    print sum_digits3(math.factorial(s))

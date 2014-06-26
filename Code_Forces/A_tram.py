N = raw_input()
N = int(N)


tout, tin = map(int, raw_input().split(" "))
maxx = tin
rem = tin

for _ in range(0, N-1):
    tout, tin = map(int, raw_input().split(" "))
    rem = rem - tout + tin
    if rem > maxx:
        maxx = rem

print maxx


#So, here how it goes. We seperate the first input from the others, in order to set a bench-mark.
#So, the inflow of first input is set as the max. capacity, and as we take in the inflow of the
#following inputs, we change the max. value depending on the (existing - output + input) formula
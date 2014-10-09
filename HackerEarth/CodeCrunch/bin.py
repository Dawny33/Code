def binary(x):
    return int(bin(x)[2:])


T = input()

while(T):
    T -= 1
    s1 = raw_input()
    s2 = raw_input()

    s1 = int(s1,2)
    s2 = int(s2,2)
    summ = s1+s2
    con = binary(summ)

    print con
    print (s1+s2)%1000000007

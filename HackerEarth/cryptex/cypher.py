T = input()

while(T):
    T -= 1
    s = raw_input()
    j = ""
    for i in range(len(s)):
        #j += chr(ord(s[i])+i)
        j += (chr((ord(s[i]) - 97 + i) % 26 + 97))
				
    print j

for T in range (0, int(raw_input())):
	n = raw_input()
	print (n[0] + str(len(n)-2) + n[len(n)-1] if len(n) > 10 else n)